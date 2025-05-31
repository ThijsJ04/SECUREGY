from flask import Flask, request, Response
import base64

app = Flask(__name__)

@app.route('/img/upload')
def upload_img():
    # Get the "filename" from the request and the "img" parameter from the request
    filename = request.args.get('filename')  # Assuming 'filename' is a query parameter in the URL
    img_data = request.files['img']          # Assuming 'img' is a file uploaded via POST request

    # Decode the image data using base64
    try:
        with open(f'./assets/img/{filename}.png', 'wb') as f:
            f.write(base64.decodebytes(img_data.read()))
    except Exception as e:
        print(e)  # Log any exceptions that occur during the save process
        return Response('An error occurred while saving the image', status=500, mimetype='text/plain')

    return Response('Image saved successfully', status=200, mimetype='application/json')