from flask import Flask, request, Response
import base64

app = Flask(__name__)

@app.route('/img/upload', methods=['GET', 'POST'])
def upload_img():
    '''
    Get the "filename" from the request and the "img" parameter from the request.
    Use base64 to decode the "img" parameter.
    Then, save the image to the file "../assets/img/{filename}.png"
    :return: a Response with status code equals to 200.
    '''
    if not request.args.get('filename') or not request.args.get('img'):
        return Response(status=400)

    filename = str(request.args.get('filename'))
    img_data = request.args.get('img')

    # Decode the base64 encoded image data
    try:
        img_bytes = base64.b64decode(img_data)
    except base64.binascii.Error as e:
        return Response(status=400, response='Invalid base64 encoding')

    # Save the image to the specified directory and filename
    import os

    # Ensure the directory exists
    save_dir = '../assets/img'
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    save_path = os.path.join(save_dir, f'{filename}.png')

    try:
        with open(save_path, 'wb') as f:
            f.write(img_bytes)
    except Exception as e:
        return Response(status=500, response='Failed to save image')

    return Response(status=200)

if __name__ == '__main__':
    app.run(debug=True)