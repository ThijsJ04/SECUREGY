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

    if request.is_json:
        data = request.get_json()
    else:
        data = request.form

    filename = data.get('filename')
    img_data = data.get('img') or data.get('image', '')

    if not filename or not img_data:
        return Response(status=400)

    try:
        decoded_img = base64.b64decode(img_data)
    except Exception as e:
        return Response(status=500, response=str(e))

    directory = os.path.dirname(f'../assets/img/{filename}.png')
    os.makedirs(directory, exist_ok=True)

    with open(f'../assets/img/{filename}.png', 'wb') as f:
        f.write(decoded_img)

    return Response(status=200)