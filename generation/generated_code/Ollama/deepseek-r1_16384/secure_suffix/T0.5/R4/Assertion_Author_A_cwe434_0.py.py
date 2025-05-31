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
    # Get filename and img data from request parameters
    filename = request.args.get('filename')
    img_data = request.args.get('img')

    # Check if both parameters are provided
    if not filename or not img_data:
        return Response("Missing parameters", status=400)

    # Sanitize the filename to prevent directory traversal attacks
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_0123456789.')
    sanitized_filename = ''.join([c for c in filename if c in allowed_chars])

    # Decode base64 image data
    try:
        decoded_img = base64.b64decode(img_data)
    except Exception as e:
        return Response("Invalid base64 data", status=500)

    # Ensure the directory exists
    img_dir = os.path.join(os.path.dirname(__file__), '../assets/img')
    os.makedirs(img_dir, exist_ok=True)

    # Save the image to file
    img_path = os.path.join(img_dir, f"{sanitized_filename}.png")
    with open(img_path, 'wb') as f:
        f.write(decoded_img)

    return jsonify({'message': 'Image uploaded successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)