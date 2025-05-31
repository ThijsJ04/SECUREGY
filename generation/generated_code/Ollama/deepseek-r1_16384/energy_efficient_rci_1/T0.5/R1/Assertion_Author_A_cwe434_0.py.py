from flask import Flask, request, Response
import base64
import os

app = Flask(__name__)

@app.route('/img/upload', methods=['GET', 'POST'])
def upload_img():
    '''
    Get the "filename" from the request and the "img" parameter from the request.
    Use base64 to decode the "img" parameter.
    Then, save the image to the file "../assets/img/{filename}.png"
    :return: a Response with status code equals to 200.
    '''
    # Get filename from request arguments or default to 'default.png'
    filename = request.args.get('filename', default='default.png')
    if not filename:
        filename = request.form.get('filename', default='default.png')

    # Try getting img_data from different sources
    img_data = None
    try:
        img_data = request.args.get('img')
        if not img_data:
            img_data = request.form.get('img')
            if not img_data:
                img_data = request.data
    except:
        pass

    if not img_data:
        return Response("Image data not provided", status=400)

    # Decode base64 string to binary data
    try:
        decoded_img = base64.b64decode(img_data)
    except base64.binascii.Error as e:
        return Response(f"Invalid base64 image data: {e}", status=400)

    # Ensure the directory exists
    dir_path = '../assets/img'
    os.makedirs(dir_path, exist_ok=True)

    # Save the decoded image to file
    file_path = os.path.join(dir_path, f"{filename}.png")
    try:
        with open(file_path, 'wb') as f:
            f.write(decoded_img)
    except Exception as e:
        return Response(f"Failed to save image: {e}", status=500)

    # Return success response
    return Response("Image uploaded successfully", status=200)