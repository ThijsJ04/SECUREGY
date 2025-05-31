from flask import Flask, request, Response
import base64
import os

app = Flask(__name__)

@app.route('/img/upload', methods=['POST'])
def upload_img():
    '''
    Get the "filename" from the request and the "img" parameter from the request.
    Use base64 to decode the "img" parameter.
    Then, save the image to the file "../assets/img/{filename}.png"
    :return: a Response with status code equals to 200.
    '''
    # Get filename and image data from request
    filename = request.args.get('filename')
    img_data = request.args.get('img')

    # Decode base64 string to bytes
    decoded_img = base64.b64decode(img_data)

    # Save the image file
    dir_path = os.path.dirname(os.path.abspath('../assets/img/'))
    if not os.path.exists(dir_path):
        os.makedirs(dir_path, exist_ok=True)

    img_path = os.path.join(dir_path, f'{filename}.png')
    with open(img_path, 'wb') as f:
        f.write(decoded_img)

    # Return success response
    return Response(
        response=json.dumps({'status': 'success', 'message': 'Image saved successfully'}),
        status=200,
        mimetype='application/json'
    )

if __name__ == '__main__':
    app.run(debug=True)