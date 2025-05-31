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
    filename = request.values.get('filename')
    img_data = request.values.get('img')

    if not filename:
        return Response(status=400, response='Filename is missing.')

    if not img_data:
        return Response(status=400, response='Image data is missing.')

    try:
        decoded_img = base64.b64decode(img_data)
    except Exception as e:
        return Response(status=400, response=str(e))

    os.makedirs('../assets/img', exist_ok=True)

    file_path = os.path.join('../assets/img', f'{filename}.png')
    with open(file_path, 'wb') as f:
        f.write(decoded_img)

    return Response()