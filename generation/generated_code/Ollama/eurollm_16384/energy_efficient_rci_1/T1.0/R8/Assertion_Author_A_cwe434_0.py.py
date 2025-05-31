from flask import Flask, request, Response
import base64

app = Flask(__name__)

@app.route('/img/upload')
def upload_img():
    filename = request.args.get("filename")
    if not filename:  # Check if the 'filename' parameter is present in the request
        return "Error: Missing required parameter - 'filename'"

    data = request.files['img']  # Get the file from the request
    if not data:
        return "Error: Missing file upload"

    with open("../assets/img/{}.png".format(filename), "wb") as f:
        data.save(f)

    # Decode the base64 string in the request body and convert it to bytes
    decoded_data = base64.decodebytes(request.get_data()).decode('utf-8')

    with open("../assets/img/{}.png".format(filename), "rb") as f:
        file_content = f.read()  # Read the content of the saved image file
    print(file_content)

    return Response(status=200, mimetype='image/png')