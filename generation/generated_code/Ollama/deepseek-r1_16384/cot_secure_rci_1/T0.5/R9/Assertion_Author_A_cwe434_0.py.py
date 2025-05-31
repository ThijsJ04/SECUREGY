from flask import Flask, request,Response
import base64

app = Flask(__name__)

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
        return Response(status=400)

    try:
        decoded_img = base64.b64decode(img_data)

        import os
        from utils import sanitize_filename

        clean_filename = sanitize_filename(filename)
        save_path = f'../assets/img/{clean_filename}.png'

        with open(save_path, 'wb') as f:
            f.write(decoded_img)

        return Response(status=200)
    except Exception as e:
        print(f"Error saving image: {e}")
        return Response(status=500)

if __name__ == '__main__':
    app.run(debug=True)