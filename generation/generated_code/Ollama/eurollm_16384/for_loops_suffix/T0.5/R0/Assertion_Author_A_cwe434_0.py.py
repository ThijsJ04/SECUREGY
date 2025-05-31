from flask import Flask, request, Response
import base64

app = Flask(__name__)

@app.route('/img/upload')
def upload_img():
    # Get the "filename" from the request
    data = request.data
    filename = request.form['filename']  # Assuming 'filename' is a form parameter

    # Decode the image base64 string to bytes
    image_bytes = base64.b64decode(data)

    # Save the image to the file "../assets/img/{filename}.png"
    try:
        with open('../assets/img/' + filename + '.png', 'wb') as f:
            f.write(image_bytes)
    except Exception as e:
        print("Error saving image:", str(e))
        return Response(status=500, mimetype='text/plain'), 500

    # Return a response with status code equals to 200
    return Response(status=200)