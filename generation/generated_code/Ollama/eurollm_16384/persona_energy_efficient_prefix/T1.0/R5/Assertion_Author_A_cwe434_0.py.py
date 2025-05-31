from io import BytesIO
import os

@app.route('/img/upload', methods=['POST'])
def upload_img():
    '''
    Get the "filename" from the request and the "img" parameter from the request.
    Use base64 to decode the "img" parameter.
    Then, save the image to the file "../assets/img/{filename}.png"
    :return: a Response with status code equals to 200.
    '''
    data = request.get_json()  # Assuming the JSON is in the form of {"filename": ..., "img": ...}
    filename = data['filename']
    img = base64.b64decode(data['img'])

    file = BytesIO(img)
    with open('../assets/img/{}.png'.format(filename), 'wb') as f:
        f.write(file.getvalue())

    return Response('', status=200, mimetype='application/json')