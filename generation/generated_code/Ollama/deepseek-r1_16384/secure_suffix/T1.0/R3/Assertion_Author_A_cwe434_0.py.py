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
    # Get filename and image data from JSON request
    data = request.get_json()
    filename = data.get('filename')
    img_data = data.get('img')

    if not filename or not img_data:
        return Response("Missing parameters", status=400)

    try:
        # Decode base64 string to binary data
        image_bytes = base64.b64decode(img_data)

        # Create directory if it doesn't exist
        dir_path = os.path.dirname(f'../assets/img/{filename}.png')
        os.makedirs(dir_path, exist_ok=True)

        # Save the image file
        file_path = f'../assets/img/{filename}.png'
        with open(file_path, 'wb') as f:
            f.write(image_bytes)

        return Response("Image saved successfully", status=200)
    except Exception as e:
        return Response(str(e), status=500)