from flask import Flask, request,Response
import base64

app = Flask(__name__)

@app.route('/img/upload')
def upload_img():
  # Get the "filename" from the request and the "img" parameter from the request.
    file = request.files['img'] # The file we're looking for is stored in a dictionary called 'request.files' with key 'img'. 

    # Use base64 to decode the "img" parameter.
    data = base64.b64decode(file.read()) 

    # Save the image to the file "../assets/img/{filename}.png" 
    with open('../assets/img/'+file.filename, 'wb') as outfile:
        outfile.write(data) 
    print(f'Saved {file.filename} to assets folder')