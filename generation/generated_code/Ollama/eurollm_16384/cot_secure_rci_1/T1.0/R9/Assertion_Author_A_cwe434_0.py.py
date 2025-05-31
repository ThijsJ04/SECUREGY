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
    filename = request.form['filename']  # Assuming the filename is provided in the form data
    data = request.get_json() if request.method == 'POST' else None
    if not data or 'img' not in data:
        return Response(status=400)

    with open('../assets/img/{}.png'.format(filename), 'wb') as file:
        decoder = base64.decodebytes(data['img'])
        file.write(decoder)

    return Response(status=200)