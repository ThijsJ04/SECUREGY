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
    # Get filename and img_data from request arguments
    filename = request.args.get('filename')
    img_data = request.args.get('img')

    if not filename or not img_data:
        return Response(status=400)  # Return 400 if missing parameters

    try:
        # Decode base64 data, replacing URL-safe characters
        decoded_img = base64.b64decode(img_data.replace('-_', '+/'))

        # Ensure the directory exists
        dir_path = os.path.dirname(os.path.abspath("../assets/img"))
        os.makedirs(dir_path, exist_ok=True)

        # Save the image
        file_path = os.path.join(dir_path, f"{filename}.png")
        with open(file_path, 'wb') as f:
            f.write(decoded_img)

        return Response(status=200)
    except Exception as e:
        print(f"Error saving image: {e}")
        return Response(status=500)