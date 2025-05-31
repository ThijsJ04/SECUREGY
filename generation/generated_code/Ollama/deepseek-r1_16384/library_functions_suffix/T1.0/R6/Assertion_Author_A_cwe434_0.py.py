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
    # Get filename and img data from request arguments
    filename = request.args.get('filename')
    img_data = request.args.get('img')

    if not filename or not img_data:
        return Response(status=400)

    try:
        # Decode the base64 encoded image data
        decoded_img = base64.b64decode(img_data)
    except base64.binascii.Error:
        return Response(status=400)

    # Ensure the directory exists
    img_dir = os.path.dirname("../assets/img")
    if not os.path.exists(img_dir):
        os.makedirs(img_dir, exist_ok=True)

    # Save the image to the specified path
    img_path = os.path.join(img_dir, f"{filename}.png")
    with open(img_path, 'wb') as img_file:
        img_file.write(decoded_img)

    # Return a successful response
    return jsonify()

if __name__ == '__main__':
    app.run(debug=True)