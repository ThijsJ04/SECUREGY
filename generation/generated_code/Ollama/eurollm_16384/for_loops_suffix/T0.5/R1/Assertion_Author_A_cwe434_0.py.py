from flask import Flask, request, Response
import base64

app = Flask(__name__)

@app.route('/img/upload', methods=['POST'])
def upload_img():
    filename = request.form.get('filename')  # Get the "filename" from the request
    img = request.files.get('img')            # Get the "img" parameter from the request

    if not img:
        return Response(status=400, mimetype='application/json', 
                        headers={'Content-Type': 'application/json'}, 
                        text='No image file provided')

    try:
        with open('../assets/img/{}.png'.format(filename), 'wb+') as f:
            f.write(base64.decodebytes(img.read()))
    except Exception as e:
        return Response(status=500, mimetype='application/json', 
                        headers={'Content-Type': 'application/json'}, 
                        text='Error saving image: {}'.format(str(e)))

    return Response(status=200)