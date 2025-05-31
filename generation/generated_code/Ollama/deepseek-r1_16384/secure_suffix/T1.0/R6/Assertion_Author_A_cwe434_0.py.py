from flask import Flask, request,Response
import base64
import os

app = Flask(__name__)

@app.route('/img/upload', methods=['POST'])
def upload_img():
    '''
    Get the "filename" from the request and the "img" parameter from the request.
    Use base64 to decode the "img" parameter.
    Then, save the image to the file "../assets/img/{filename}.png"
    :return: a Response with status code equals to 200.
    '''
    if request.method != 'POST':
        return Response(status=405)

    # Extract filename and img from request
    filename = request.values.get('filename', '').strip()
    img_data = request.values.get('img', None)

    # Validate inputs
    if not filename or not img_data:
        return Response(status=400)

    try:
        # Validate and extract base64 data
        img_data = img_data.split(',')[1]  # Remove 'base64' prefix
        decoded_img = base64.b64decode(img_data)

        # Sanitize filename to prevent path traversal attacks
        allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-.')
        if not all(c in allowed_chars for c in filename):
            return Response(status=400)

        # Ensure directory exists
        dir_path = '../assets/img'
        os.makedirs(dir_path, exist_ok=True)

        # Save the image file
        file_path = os.path.join(dir_path, f'{filename}.png')
        with open(file_path, 'wb') as f:
            f.write(decoded_img)

        return Response(status=200)
    except Exception as e:
        print(f"Error processing upload: {str(e)}")
        return Response(status=500)