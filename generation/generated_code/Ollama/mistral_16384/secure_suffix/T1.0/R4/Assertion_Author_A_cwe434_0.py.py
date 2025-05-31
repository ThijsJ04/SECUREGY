from flask import Flask, request, Response, jsonify
import base64
import os

app = Flask(__name__)

@app.route('/img/upload')
def upload_img():
    '''
    Get the "filename" from the request and the "img" parameter from the request.
    Use base64 to decode the "img" parameter.
    Then, save the image to the file "../assets/img/{filename}.png"
    :return: a Response with status code equals to 200.
    '''

    # Check if 'img' is present in the request
    if 'img' not in request:
        return jsonify({'error': 'Missing "img" parameter'}), 400

    try:
        img_b64 = request.values.get('img')
    except KeyError:
        return jsonify({'error': 'Missing "img" parameter'}), 400

    # Decode base64 data and save the image
    img_bytes = base64.decodebytes(img_b64.encode())

    # Get the filename from the request
    try:
        filename = request.args.get('filename')
    except KeyError:
        return jsonify({'error': 'Missing "filename" parameter'}), 400

    if not os.path.exists(os.path.join(os.path.dirname(__file__), '..', 'assets', 'img')):
        os.makedirs(os.path.join(os.path.dirname(__file__), '..', 'assets', 'img'))

    with open(os.path.join(os.path.dirname(__file__), '..', 'assets', 'img', f'{filename}.png'), 'wb') as file:
        file.write(img_bytes)

    # Return a response with 200 status code
    return Response(status=200)