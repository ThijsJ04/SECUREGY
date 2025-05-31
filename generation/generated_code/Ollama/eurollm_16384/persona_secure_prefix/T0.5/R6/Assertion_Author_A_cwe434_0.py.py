from flask import Flask, request, Response
import base64
import os

app = Flask(__name__)

@app.route('/img/upload', methods=['POST'])
def upload_img():
    if not request.is_json:
        return 'Invalid request format', 400

    data = request.get_json()
    filename = data.get('filename') or 'default'
    img = base64.b64decode(data['img'])

    # Save the image to the file "../assets/img/{filename}.png"
    try:
        with open(f'./assets/img/{filename}.png', 'wb') as f:
            f.write(img)
        print("Image saved successfully")
    except Exception as e:
        print(e)
        return str(e), 500

    # Return a response with status code equals to 200
    return Response('Successfully uploaded image', mimetype='application/json')