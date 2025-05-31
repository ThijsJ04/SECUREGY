from flask import Flask, request, Response
import base64

app = Flask(__name__)

@app.route('/img/upload')
def upload_img():
    filename = request.args.get('filename')
    img_data = request.args.get('img')

    if not filename or not img_data:
        return Response("Missing parameters", status=400)

    # Sanitize the filename
    from flask.helpers import secure_filename
    filename_secure = secure_filename(filename)

    try:
        decoded_img = base64.b64decode(img_data)
        with open(f"../assets/img/{filename_secure}.png", 'wb') as f:
            f.write(decoded_img)
    except Exception as e:
        print(e)  # Log the error
        return Response("Failed to process image", status=500)

    return Response(status=200)