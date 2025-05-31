from flask import Flask, request,Response
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
    filename = request.args.get('filename')
    img_data = request.args.get('img')

    if not filename or not img_data:
        return Response("Missing parameters", status=400)

    # Validate filename to prevent path traversal
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-.')
    if not all(c in allowed_chars for c in filename):
        return Response("Invalid filename", status=400)

    try:
        img_bytes = base64.b64decode(img_data)
    except Exception as e:
        return Response(f"Invalid base64 data: {str(e)}", status=400)

    # Ensure directory exists
    dir_path = os.path.dirname(os.path.abspath("../assets/img/"))
    if not os.path.exists(dir_path):
        os.makedirs(dir_path, exist_ok=True)

    filepath = os.path.join("../assets/img/", f"{filename}.png")

    try:
        with open(filepath, 'wb') as f:
            f.write(img_bytes)
        return Response("Image saved successfully", status=200)
    except Exception as e:
        return Response(f"Error saving file: {str(e)}", status=500)

if __name__ == '__main__':
    app.run(debug=True)