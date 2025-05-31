from flask import Flask, request, Response
import base64

app = Flask(__name__)

@app.route('/img/upload')
def upload_img():
    filename = request.values.get('filename')
    img_data = request.values.get('img')

    if not filename or not img_data:
        return Response(status=400)

    try:
        decoded_img = base64.b64decode(img_data)
        path = f"../assets/img/{filename}.png"
        with open(path, 'wb') as f:
            f.write(decoded_img)
        return Response()
    except Exception as e:
        print(e)
        return Response(status=500)