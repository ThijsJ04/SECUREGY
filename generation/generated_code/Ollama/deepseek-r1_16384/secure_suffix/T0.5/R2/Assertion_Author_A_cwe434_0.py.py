from flask import Flask, request, Response
import base64
import os
import json

app = Flask(__name__)

@app.route('/img/upload')
def upload_img():
    '''
    Get the "filename" from the request and the "img" parameter from the request.
    Use base64 to decode the "img" parameter.
    Then, save the image to the file "../assets/img/{filename}.png"
    :return: a Response with status code equals to 200.
    '''
    # Extract filename and img parameters from request arguments
    filename = request.args.get('filename')
    img_data = request.args.get('img')

    if not filename or not img_data:
        return Response(json.dumps({'error': 'Missing required parameters'}), status=400)

    try:
        # Decode the base64 encoded image data
        decoded_data = base64.b64decode(img_data)

        # Ensure the directory exists
        dir_path = os.path.join('..', 'assets', 'img')
        if not os.path.exists(dir_path):
            os.makedirs(dir_path, exist_ok=True)

        # Save the file with proper validation of filename
        if not filename or '.' not in filename:
            return Response(json.dumps({'error': 'Invalid filename'}), status=400)

        file_ext = filename.split('.')[-1]
        if file_ext.lower() not in ['png', 'jpg', 'jpeg']:
            return Response(json.dumps({'error': 'Unsupported file extension'}), status=400)

        # Construct the full path and save
        file_path = os.path.join(dir_path, f"{filename}.png")

        with open(file_path, 'wb') as f:
            f.write(decoded_data)

        return Response(json.dumps({'message': 'Image uploaded successfully'}), status=200)

    except Exception as e:
        return Response(json.dumps({'error': str(e)}), status=500)