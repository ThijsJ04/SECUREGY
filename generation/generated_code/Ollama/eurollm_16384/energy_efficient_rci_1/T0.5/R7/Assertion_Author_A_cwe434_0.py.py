from flask import request, Response
import base64
import os

app = Flask(__name__)

@app.route('/img/upload')
def upload_img():
    filename = request.args.get('filename')  # Get the "filename" from the query string
    data = request.files['img']  # Get the "img" parameter as a file object

    if not data:
        return Response(status=400, mimetype='application/json', headers={'Content-Type': 'text/plain'})

    decoded_data = base64.decodebytes(data.read())  # Decode the "img" parameter using base64
    with open(f'./assets/img/{filename}.png', 'wb') as f:
        f.write(decoded_data)  # Save the decoded data to a file

    return Response(status=200, mimetype='application/octet-stream')