from flask import Flask, request,Response
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
    img_data = request.args.get('img')

    # Ensure the directory exists
    os.makedirs('../assets/img', exist_ok=True)

    # Sanitize filename to prevent path traversal
    safe_filename = filename.replace('/', '').replace('\\', '')

    try:
        # Add missing padding if necessary and decode
        img_bytes = base64.b64decode(img_data)

        with open(f'../assets/img/{safe_filename}.png', 'wb') as f:
            f.write(img_bytes)

        return Response('', status=200)
    except Exception as e:
        return Response(str(e), status=400)

if __name__ == '__main__':
    app.run(debug=True)