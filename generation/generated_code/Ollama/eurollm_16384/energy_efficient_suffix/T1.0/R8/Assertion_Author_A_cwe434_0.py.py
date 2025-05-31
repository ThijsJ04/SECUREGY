from flask import Flask, request, Response
import base64

app = Flask(__name__)

@app.route('/img/upload')
def upload_img():
    if 'filename' in request.files:  # Check if the 'filename' key exists in the request data
        file = request.files['filename']  # Get the file from the request
        print(f"Uploaded file: {file}")

        # Convert image to base64 string
        img_data = ''
        content = bytearray()
        with open('../assets/img/' + file.filename, 'wb') as f:
            f.write(content)  # Write the file contents to the file
        img_data = base64.b64encode(content).decode("utf-8")
        print(f"Decoded image string: {img_data}")
    else:
        print("No image data found.")

    # Create a response with a JSON payload containing the filename and an empty message
    content = "Filename: {}, Message: {}".format(file.filename, '')
    return Response(response=content.encode('utf-8'), status=200, mimetype='application/json')