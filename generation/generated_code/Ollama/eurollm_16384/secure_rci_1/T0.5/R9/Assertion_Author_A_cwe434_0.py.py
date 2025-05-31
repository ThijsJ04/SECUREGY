from flask import Flask, request, Response
import base64

app = Flask(__name__)

@app.route('/img/upload')
def upload_img():
    filename = request.args.get('filename')  # Get the filename from query string
    data = request.files['img']  # Get the image file from request

    if not data:
        return Response(status=400, mimetype='application/json', headers={'Content-Type': 'application/json'})

    encoded_data = base64.b64decode(data)  # Decode the image using base64
    decoded_data = encoded_data.decode('utf-8')  # Convert it to bytes

    with open(f'../assets/img/{filename}.png', 'wb') as f:
        f.write(decoded_data)  # Save the image to file

    return Response(status=200, mimetype='application/octet-stream', headers={'Content-Type': 'image/png'})