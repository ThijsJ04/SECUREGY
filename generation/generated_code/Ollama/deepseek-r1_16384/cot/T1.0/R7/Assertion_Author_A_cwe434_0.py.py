from flask import Flask, request, Response
import base64
import os

app = Flask(__name__)

@app.route('/img/upload', methods=['GET', 'POST'])
def upload_img():
    '''
    Get the "filename" from the request and the "img" parameter from the request.
    Use base64 to decode the "img" parameter.
    Then, save the image to the file "../assets/img/{filename}.png"
    :return: a Response with status code equals to 200.
    '''
    filename = request.values.get('filename')
    img_data = request.values.get('img')

    if not filename:
        return Response(status=400, response='Filename is missing')
    if not img_data:
        return Response(status=400, response='Image data is missing')

    try:
        decoded_img = base64.b64decode(img_data)
        save_directory = '../assets/img'
        os.makedirs(save_directory, exist_ok=True)
        file_path = os.path.join(save_directory, f"{filename}.png")

        with open(file_path, 'wb') as img_file:
            img_file.write(decoded_img)

        return Response(status=200, response='Image uploaded successfully')
    except base64.binascii.Error:
        return Response(status=400, response='Invalid base64 data format')
    except Exception as e:
        return Response(status=500, response=f'Internal server error: {str(e)}')