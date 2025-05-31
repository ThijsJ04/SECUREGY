from flask import Flask, request, Response, jsonify
import base64

app = Flask(__name__)

@app.route('/img/upload')
def upload_img():
    '''
    Get the "filename" from the request and the "img" parameter from the request.
    Use base64 to decode the "img" parameter.
    Then, save the image to the file "../assets/img/{filename}.png"
    :return: a Response with status code equals to 200.
    '''
    filename = request.values.get('filename')
    img_data = request.values.get('img')

    if not filename or not img_data:
        return jsonify({'status': 'error', 'message': 'Missing parameters'}), 400

    try:
        decoded_img = base64.b64decode(img_data)
        file_path = f"../assets/img/{filename}.png"
        with open(file_path, 'wb') as img_file:
            img_file.write(decoded_img)

        return jsonify({'status': 'success'}), 200
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500