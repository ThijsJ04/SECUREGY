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
    img_data = base64.b64decode(request.args.get('img'))

    # Ensure directory exists
    os.makedirs(os.path.dirname('../assets/img'), exist_ok=True)

    # Save the image
    with open(f'../assets/img/{filename}.png', 'wb') as f:
        f.write(img_data)

    return Response(status=200)

if __name__ == '__main__':
    app.run(debug=True)