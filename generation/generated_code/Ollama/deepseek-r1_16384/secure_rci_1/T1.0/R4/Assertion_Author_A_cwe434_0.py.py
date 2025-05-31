from flask import Flask, request, Response
import base64

app = Flask(__name__)

@app.route('/img/upload', methods=['POST'])
def upload_img():
    '''
    Get the "filename" from the request and the "img" parameter from the request.
    Use base64 to decode the "img" parameter.
    Then, save the image to the file "../assets/img/{filename}.png"
    :return: a Response with status code equals to 200.
    '''
    if not request.data:
        return Response("Bad request", status=400)

    filename = request.args.get('filename', '')
    img_data = request.form.get('img', '') or request.args.get('img', '')

    if not filename or not img_data:
        return Response("Missing parameters", status=400)

    try:
        img_bytes = base64.b64decode(img_data)

        # Ensure the directory exists
        import os
        dir_path = '../assets/img'
        os.makedirs(dir_path, exist_ok=True)

        file_path = os.path.join(dir_path, f"{filename}.png")
        with open(file_path, 'wb') as f:
            f.write(img_bytes)

        return jsonify({'message': 'Image uploaded successfully'})
    except Exception as e:
        return Response(str(e), status=500)

if __name__ == '__main__':
    app.run(debug=True)