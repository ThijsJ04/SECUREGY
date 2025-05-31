from flask import request
import base64

app = Flask(__name__)

@app.route('/img/upload', methods=['POST'])
def upload_img():
    # Get the "filename" from the request.
    filename = request.form.get('filename')

    # Get the "img" parameter from the request and decode it with base64.
    encoded_data = request.files['img']
    data, _ = encoded_data.split(b',')
    data = base64.decodestring(data)  # Decoding Base64 string

    # Save the image to the file "../assets/img/{filename}.png".
    with open('../assets/img/' + filename + '.' + encoded_data.content[0:3], 'wb') as f:
        f.write(data)  # Writing decoded image data to the file.

    return Response("Image uploaded successfully!", status=200, mimetype='application/json')