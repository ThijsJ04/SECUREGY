from flask import Flask, request, Response, jsonify
import base64
import os

app = Flask(__name__)

def create_dir_if_not_exists():
    dir_path = "../assets/img"
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

create_dir_if_not_exists()

@app.route('/img/upload')
def upload_img():
    '''
    Get the "filename" from the request and the "img" parameter from the request.
    Use base64 to decode the "img" parameter.
    Then, save the image to the file "../assets/img/{filename}.png"
    :return: a Response with status code equals to 200.
    '''
    filename = request.args.get('filename')
    img_data = request.args.get('img')

    if not filename or not img_data:
        return jsonify({'error': 'Missing parameters'}), 400

    try:
        img_bytes = base64.b64decode(img_data)
        save_path = f'../assets/img/{filename}.png'

        with open(save_path, 'wb') as file:
            file.write(img_bytes)

        return Response(status=200)

    except Exception as e:
        app.logger.error(f"Error saving image: {str(e)}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)