from flask import Flask, request,Response
import base64
app = Flask(__name__)
@app.route('/img/upload', methods=['POST']) # Only support post method for uploading an image.
def upload_img():
    img=request.files['img'] # Getting the img parameter from the request.
    data = base64.b64decode(img.read())  # Decoding the image using base64.
    with open('../assets/img/{filename}.png'.format(filename=img.filename), 'wb') as f: # Saving the decoded image to a file named "{filename}.png".
        f.write(data) 
    return Response("Img saved successfully!", mimetype='image/png') # Returning the response with status code equals to 200 and indicating that the img has been saved successfully.