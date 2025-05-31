from flask import Flask, request, Response
import base64
import os

app = Flask(__name__)

@app.route('/img/upload', methods=['POST'])
def upload_img():
    '''
    Use the "filename" from the request and the "img" parameter to save an image.
    The response will be a 200 status code and contain a dictionary with the file name and the saved image as its value.
    :return: A Response with a JSON representation of {"success": True, "filename": <filename>, "image": <image_data>}
    '''
    # Get the filename from the request
    filename = request.form['filename']
    # Get the image data from the request using base64
    try:
        img_data = request.files['img'].read()
        # Save the image to the assets folder with the given name
        savepath = os.path.join('..', 'assets', f"{filename}.png")
        with open(savepath, "wb") as outfile:
            outfile.write(img_data)
    except Exception as e:
        # Handle any exceptions that may occur during image upload and response with a 406 status code
        print(f"Error saving the image: {e}")
        return Response("", 406, {'Content-Type': 'text/plain'})
    return Response({"success": True, "filename": filename, "image": img_data}, 200)