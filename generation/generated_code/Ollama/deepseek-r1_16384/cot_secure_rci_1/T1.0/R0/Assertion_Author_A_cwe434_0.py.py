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
    # Extract filename and img from request parameters
    filename = request.args.get('filename')
    img_data = request.args.get('img', '')

    try:
        # Decode the base64 encoded image data
        decoded_img = base64.b64decode(img_data)

        # Ensure the directory exists
        os.makedirs('../assets/img', exist_ok=True)

        # Save the image to the specified file path
        file_path = f'../assets/img/{filename}.png'
        with open(file_path, 'wb') as img_file:
            img_file.write(decoded_img)

        # Return a 200 status response
        return Response('', status=200)
    except Exception as e:
        print(f"Error processing image upload: {e}")
        return Response('Internal Server Error', status=500)