from flask import Flask, request, Response
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
    img_str = request.args.get('img')

    if not filename:
        return Response("Filename is required.", status=400)
    if not img_str:
        return Response("Image data is required.", status=400)

    try:
        decoded_image = base64.b64decode(img_str)
    except Exception as e:
        return Response(f"Invalid base64 data: {e}", status=400)

    # Ensure the target directory exists
    save_directory = os.path.dirname('../assets/img/')
    if not os.path.exists(save_directory):
        os.makedirs(save_directory, exist_ok=True)

    file_path = f'../assets/img/{filename}.png'

    try:
        with open(file_path, 'wb') as f:
            f.write(decoded_image)
    except Exception as e:
        return Response(f"Failed to save image: {e}", status=500)

    return Response('', status=200)