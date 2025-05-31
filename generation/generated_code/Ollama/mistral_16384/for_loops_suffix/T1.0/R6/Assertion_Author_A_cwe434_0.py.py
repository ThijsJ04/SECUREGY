import flask
import base64
from io import BytesIO
import os

app = Flask(__name__)

@app.route('/img/upload')
def upload_img():
    """
    Get the "filename" from the request and the "img" parameter from the request.
    Use base64 to decode the "img" parameter.
    Then, save the image to the file "../assets/img/{filename}.png"
    :return: a Response with status code equals to 200.
    """
    filename = flask.request.args.get('filename')
    img_str = flask.request.form['img']
    img_data = base64.b64decode(img_str)

    with BytesIO(img_data) as output:
        output.name = f"{filename}.png"
        output.seek(0)
        with open(os.path.join('../assets/img', filename + '.png'), 'wb') as f:
            f.write(output.read())

    return flask.Response(status=200)