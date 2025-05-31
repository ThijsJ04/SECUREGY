from flask import Flask, request,Response
import base64
app = Flask(__name__)

@app.route('/img/upload')
def upload_img():
  filename = request.form['filename'] # Get the "filename" from the request
  with open("../assets/img/{}.png".format(filename), "wb") as f:
    # Read image file into base64 string
    data = request.data
    decoded_image = base64.b64decode(data) # Decode the "img" parameter using base64
    f.write(decoded_image) # Write the decoded data to the file
  return Response("Successfully saved image!", status=200)