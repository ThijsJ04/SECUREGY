from flask import Flask, request, Response, current_app
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
    filename = request.args.get('filename', None)
    if not filename:
        return Response(status=400)

    img_param = request.params.get('img')
    if not img_param:
        return Response(status=400)

    try:
        decoded_img = base64.b64decode(img_param)
    except Exception as e:
        return Response(response=str(e), status=500)

    img_path = os.path.join(current_app.root_path, '..', 'assets', 'img', f"{filename}.png")
    with open(img_path, "wb") as f:
        f.write(decoded_img)

    return Response(status=200)