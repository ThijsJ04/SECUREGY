from flask import Flask, request, Response
import base64

app = Flask(__name__)

@app.route('/img/upload', methods=['POST'])
def upload_img():
    '''
    Get the "filename" from the request and the "img" parameter from the request.
    Use base64 to decode the "img" parameter.
    Then, save the image to the file "../assets/img/{filename}.png"
    :return: a Response with status code equals to 200.
    '''
    filename = request.values.get('filename')
    img_str = request.values.get('img')

    if not filename or not img_str:
        return Response("Missing parameters", status=400)

    try:
        img_data = base64.b64decode(img_str)
        with open(f'../assets/img/{filename}.png', 'wb') as f:
            f.write(img_data)
        return Response("Image uploaded successfully", status=200)
    except Exception as e:
        return Response(str(e), status=500)