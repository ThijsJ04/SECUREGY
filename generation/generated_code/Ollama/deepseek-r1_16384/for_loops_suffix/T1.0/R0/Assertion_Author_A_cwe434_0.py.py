from flask import Flask, request, Response
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
    # Get filename and img parameters
    filename = request.form.get('filename')
    img_base64 = request.form.get('img')

    if not filename or not img_base64:
        return Response("Missing parameters", 400)

    try:
        # Decode the base64 encoded image data
        decoded_img = base64.b64decode(img_base64)

        # Save the image to specified directory and file
        file_path = f"../assets/img/{filename}.png"
        with open(file_path, 'wb') as f:
            f.write(decoded_img)

        return Response("Image uploaded successfully", 200, content_type='text/plain')
    except Exception as e:
        app.logger.error(f"Error uploading image: {str(e)}")
        return Response("Failed to upload image", 500)

if __name__ == '__main__':
    app.run(debug=True)