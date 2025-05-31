from flask import Flask, request, Response
import base64

app = Flask(__name__)

@app.route('/img/upload')
def upload_img():
    filename = request.url_root.split('?')[0].split('#')[-1]  # Get filename from the URL
    data = request.get_data()  # Get image data (base64 encoded) from request payload

    # Decode base64 and save as image to assets folder
    image_bytes = base64.b64decode(data)
    img_filepath = os.path.join('assets', filename + '.png')  # Create file path for the image
    open(img_filepath, "wb").write(image_bytes)

    # Return response with status code 200
    return Response(status=200)