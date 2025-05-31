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
    filename = request.args.get('filename')
    img_data = request.args.get('img')

    # Decode the base64 encoded string
    decoded_data = base64.b64decode(img_data, validate=True)

    # Save the image to the specified location
    file_path = f'../assets/img/{filename}.png'
    with open(file_path, 'wb') as f:
        f.write(decoded_data)

    return Response('', status=200)