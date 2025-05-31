from flask import Flask, request,Response
import base64

app = Flask(__name__)

@app.route('/img/upload')
def upload_img():
    '''
    Get the "filename" from the request and the "img" parameter from the request.
    Use base64 to decode the "img" parameter.
    Then, save the image to the file "../assets/img/{filename}.png"
    :return: a Response with status code equals to 200.
    '''
    filename = request.args.get('filename', 'unknown')
    img_data = request.args.get('img', '')

    try:
        # Handle base64 decoding and padding
        decoded_img = base64.b64decode(img_data)

        # Save the image to file
        save_path = f'../assets/img/{filename}.png'
        with open(save_path, 'wb') as img_file:
            img_file.write(decoded_img)

        return Response('', status=200)

    except ValueError:
        # Invalid base64 data
        return Response('Invalid image format', status=500)
    except Exception as e:
        # General error
        return Response('Error saving image', status=500)