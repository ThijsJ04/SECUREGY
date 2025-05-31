from flask import Flask, request, Response, jsonify
import base64
import os

app = Flask(__name__)

@app.route('/img/upload')
def upload_img():
    '''
    Get the "filename" and "img" parameters from the request.
    Decode the "img" parameter using base64.
    Save the decoded image to the file "../assets/img/{filename}.png".
    Return a Response with status code 200 on success or 400 on error.
    '''
    filename = request.args.get('filename')
    img_data = request.args.get('img')

    if not filename or not img_data:
        return jsonify({'error': 'Missing parameters'}), 400

    try:
        # Decode the base64 image data
        decoded_img = base64.b64decode(img_data)

        # Construct the file path
        save_path = os.path.join('../assets/img', f'{filename}.png')

        # Save the image to the specified directory
        with open(save_path, 'wb') as f:
            f.write(decoded_img)

        return Response(status=200)
    except base64.binascii.Error:
        return jsonify({'error': 'Invalid base64 data'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500