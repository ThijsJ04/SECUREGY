from flask import Flask, request,Response, send_file
import base64

app = Flask(__name__)

@app.route('/img/upload', methods=['POST'])
def upload_img():
    if not request.files:
        return Response(status=400, mimetype='application/json')

    filename = request.form.get('filename')
    data = request.data

    # Get the first part of the data before 'data=' and discard it
    data_length = len(data)
    data = data[1:len(data)-2]

    # Decode the Base64 encoded image data
    img = base64.b64decode(data).tobytes()

    # Save the image to the file "../assets/img/{filename}.png"
    with open('../assets/img/' + filename + '.png', 'wb') as f:
        f.write(img)

    return send_file('../assets/img/' + filename + '.png')