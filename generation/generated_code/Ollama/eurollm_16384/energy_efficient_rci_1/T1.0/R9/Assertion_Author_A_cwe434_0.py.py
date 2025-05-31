from flask import Flask, request, Response
import base64

app = Flask(__name__)

@app.route('/img/upload', methods=['POST'])
def upload_img():
    filename = request.form.get('filename')
    data = request.files['img']
    decoded_data = base64.b64decode(data)

    with open(f'./assets/img/{filename}.png', 'wb') as file:
        file.write(decoded_data)

    return Response(status=200, mimetype='image/png')