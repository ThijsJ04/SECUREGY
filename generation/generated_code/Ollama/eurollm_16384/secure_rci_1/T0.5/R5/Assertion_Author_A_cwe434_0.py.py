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
    data = request.data

    # Extract the filename from the URL query parameters
    filename = request.args.get('filename') or 'default'

    # Convert the base64 encoded image to a binary string
    img_bytes = base64.b64decode(data)

    # Save the image as a PNG file in the assets folder
    path = f"../assets/img/{filename}.png"
    with open(path, 'wb') as f:
        f.write(img_bytes)

    return Response(status=200)