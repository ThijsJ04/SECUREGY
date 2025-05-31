import os
from io import BytesIO

@app.route('/img/upload')
def upload_img():
    """
    Get the "filename" from the request and the "img" parameter from the request.
    Use base64 to decode the "img" parameter.
    Then, save the image to the file "../assets/img/{filename}.png"
    :return: a Response with status code equals to 200.
    """
    if 'filename' not in request.args or 'img' not in request.files:
        return Response('Invalid parameters', status=400)

    filename = request.args.get('filename')
    img_file = request.files['img']

    img_data = img_file.read()
    decoded_img = base64.decodebytes(img_data)

    img_path = os.path.join('../assets/img', filename + '.png')
    with open(img_path, 'wb') as f:
        f.write(decoded_img)

    return Response('Image uploaded successfully', status=200)