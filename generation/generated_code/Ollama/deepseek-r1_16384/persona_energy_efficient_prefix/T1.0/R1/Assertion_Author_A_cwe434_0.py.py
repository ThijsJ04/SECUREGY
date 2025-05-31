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
    # Get filename and img data from request parameters
    try:
        if 'img' in request.args:
            img_str = request.args['img']
        elif 'img' in request.form:
            img_str = request.form['img']
        else:
            return Response('Img parameter not found', 400)

        if 'filename' in request.args:
            filename = request.args['filename']
        elif 'filename' in request.form:
            filename = request.form['filename']
        else:
            return Response('Filename parameter not found', 400)

        # Decode base64 string
        img_data = base64.b64decode(img_str)

        # Save image to file
        dir_path = '../assets/img/'
        if not os.path.exists(dir_path):
            os.makedirs(dir_path, exist_ok=True)

        file_path = os.path.join(dir_path, f'{filename}.png')
        with open(file_path, 'wb') as f:
            f.write(img_data)

        return Response('Image saved successfully', 200)
    except Exception as e:
        return Response(str(e), 500)

if __name__ == '__main__':
    app.run(debug=True)