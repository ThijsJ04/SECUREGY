from flask import Flask, request, Response
import base64

app = Flask(__name__)

@app.route('/img/upload')
def upload_img():
    filename = request.args.get('filename')
    img_str = request.args.get('img')

    if not filename or not img_str:
        return Response(status=400)

    try:
        decoded_img = base64.b64decode(img_str)
    except Exception as e:
        app.logger.error(f"Base64 decoding failed: {e}")
        return Response(status=400)

    save_path = f'../assets/img/{filename}.png'
    with open(save_path, 'wb') as f:
        f.write(decoded_img)

    return Response()

# The function retrieves filename and img from request parameters,
# decodes the base64 string, saves the image to the specified path,
# and returns a 200 status code response.