from flask import Flask, request,Response
import base64

app = Flask(__name__)

@app.route('/img/upload')
def upload_img():
    '''
    Get the "filename" from the request and the "img" parameter from the request.
    Use base64 to decode the "img" parameter.
    Then, save the image to the file "../assets/img/{filename}.png"
    :return: a Response with status code equals to 200.
    '''
    if not request.json:
        return 'Expected JSON data', 400
    filename = request.json.get('filename')
    img_data = request.json.get('img')

    if not filename or not img_data:
        return 'Missing parameters', 400

    try:
        decoded_img = base64.b64decode(img_data)
        with open(f'../assets/img/{filename}.png', 'wb') as f:
            f.write(decoded_img)
    except Exception as e:
        print(e)
        return 'Failed to process image', 500

    return Response('Image saved successfully', status=200)