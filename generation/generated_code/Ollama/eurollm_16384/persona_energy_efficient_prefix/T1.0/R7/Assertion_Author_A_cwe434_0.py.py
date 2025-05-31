from flask import Flask, request, Response
import base64
app = Flask(__name__)

@app.route('/img/upload')
def upload_img():
   # Get the "filename" from the request and the "img" parameter from the request
   filename = request.args.get("filename")
   imgdata = request.form["img"]

   # Use base64 to decode the "img" parameter
   encoded_image = str(base64.b64decode(imgdata))

   # Save the image to the file "../assets/img/{filename}.png"
   with open(f"./assets/img/{filename}.png", "wb") as f:
      f.write(encoded_image)

    # Return a response with status code equals to 200
    return Response("Image uploaded successfully!", mimetype='image/png')