from flask import Flask, request, Response
import base64
import os

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

    try:
        # Decode base64 data
        image_bytes = base64.b64decode(img_data)

        # Ensure the directory exists
        dir_path = os.path.join(os.path.dirname(__file__), "..", "assets", "img")
        os.makedirs(dir_path, exist_ok=True)

        # Save the file
        file_path = os.path.join(dir_path, f"{filename}.png")
        with open(file_path, 'wb') as f:
            f.write(image_bytes)

        return Response(status=200)
    except Exception as e:
        print(f"Error processing image upload: {e}")
        return Response(status=500)

if __name__ == '__main__':
    app.run(debug=True)