from flask import Flask, request, Response
import base64

app = Flask(__name__)

@app.route('/img/upload', methods=['POST'])
def upload_img():
    filename = request.form.get('filename')  # Get the "filename" from the request
    img = base64.b64decode(request.data)  # Decode the "img" parameter using base64

    try:
        with open(f'../assets/img/{filename}.png', 'wb') as file:
            file.write(img)  # Save the image to the file
    except Exception as e:
        print('Error saving image:', str(e))

    return Response(status=200, mimetype='image/png')