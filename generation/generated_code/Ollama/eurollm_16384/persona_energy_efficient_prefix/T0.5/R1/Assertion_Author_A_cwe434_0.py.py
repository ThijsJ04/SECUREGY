from flask import Flask, request, Response
import base64

app = Flask(__name__)

@app.route('/img/upload')
def upload_img():
    filename = request.args.get('filename')  # Get the "filename" from the request
    img = request.files['img']  # Get the "img" parameter from the request

    if not filename:
        return Response(status=400, mimetype='application/json', headers={'Content-Type': 'application/json'})

    decoded_img = base64.b64decode(img.read())  # Decode the "img" parameter using base64
    with open(f'./assets/img/{filename}.png', 'wb') as f:
        f.write(decoded_img)  # Save the decoded image to a file

    return Response(status=200, mimetype='application/json', headers={'Content-Type': 'application/json'}, data={'message': 'Image uploaded successfully'})