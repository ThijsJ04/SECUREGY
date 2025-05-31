from flask import Flask, request,Response
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

    if not filename or not img_data:
        return Response("Missing parameters", status=400)

    try:
        # Decode the base64 image data
        decoded_img = base64.b64decode(img_data)

        # Ensure the directory exists
        dir_path = os.path.dirname("../assets/img")
        if not os.path.exists(dir_path):
            os.makedirs(dir_path, exist_ok=True)

        # Save the file
        file_path = os.path.join("../assets/img", f"{filename}.png")
        with open(file_path, 'wb') as f:
            f.write(decoded_img)

        return Response(status=200)
    except Exception as e:
        print(f"Error saving image: {e}")
        return Response("Failed to process image", status=500)

if __name__ == '__main__':
    app.run(debug=True)