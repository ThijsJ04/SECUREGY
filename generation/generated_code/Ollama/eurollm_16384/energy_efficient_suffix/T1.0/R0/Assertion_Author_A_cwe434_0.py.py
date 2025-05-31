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
    # Check if the request has been made and the correct method was used (POST)
    if not request.method == 'POST' or not request.is_json:
        return Response(status=405, mimetype='application/problem+json')

    # Get the filename from the JSON payload of the request
    try:
        data = request.get_json()
        filename = data['filename']
    except KeyError:
        return Response(status=405, mimetype='application/problem+json')

    # Base64 decode the image data and check if it's valid
    try:
        decoder = base64.b64decoder()
        img_data = decoder.decodestring(request.files['img'].read())
    except TypeError as e:
        return Response(status=500, mimetype='application/problem+json')
    if not img_data:  # Check if base64 decode is valid and returns a string
        return Response(status=405, mimetype='application/problem+json')

    # Create the filename with the correct extension and path
    asset_path = '../assets/img' + '/' + str(filename) + '.' + request.files['img'].content_type.split(';')[0] # Adding '.' + image type to the file name, like .jpg, .png etc.
    # Save the decoded image to the file path
    open(asset_path, 'wb').write(img_data)
    return Response(status=200, mimetype='application/problem+json')