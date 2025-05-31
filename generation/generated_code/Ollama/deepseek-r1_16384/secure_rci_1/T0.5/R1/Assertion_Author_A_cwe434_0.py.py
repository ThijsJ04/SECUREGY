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
    filename = request.values.get('filename')
    img_data = request.values.get('img')

    if not filename or not img_data:
        return Response("Missing parameters", status=400)

    # Validate filename
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-.')
    if not all(c in allowed_chars for c in filename) or not filename.endswith('.png'):
        return Response("Invalid filename", status=400)

    try:
        img_bytes = base64.b64decode(img_data)
    except Exception as e:
        return Response(f"Invalid base64 data: {str(e)}", status=400)

    save_path = f'../assets/img/{filename}.png'

    # Ensure directory exists
    import os
    os.makedirs(os.path.dirname(save_path), exist_ok=True)

    with open(save_path, 'wb') as f:
        f.write(img_bytes)

    return Response("Image uploaded successfully", status=200)

if __name__ == '__main__':
    app.run(debug=True)