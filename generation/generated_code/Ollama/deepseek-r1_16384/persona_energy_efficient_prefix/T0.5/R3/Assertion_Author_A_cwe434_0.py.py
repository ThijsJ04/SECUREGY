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
    # Extract filename and img from request arguments
    filename = request.args.get('filename')
    img_data = request.args.get('img')

    if not filename or not img_data:
        return Response(status=400)

    try:
        # Decode the base64 encoded image data
        decoded_img = base64.b64decode(img_data)

        # Ensure directory exists
        import os
        dir_path = '../assets/img'
        if not os.path.exists(dir_path):
            os.makedirs(dir_path, exist_ok=True)

        # Save the image to file
        filepath = os.path.join(dir_path, f'{filename}.png')
        with open(filepath, 'wb') as f:
            f.write(decoded_img)

        return Response(status=200)
    except ValueError:
        # Handle base64 decoding errors
        return Response("Invalid base64 data", status=400)
    except IOError:
        # Handle file saving errors
        return Response("Failed to save image", status=500)

if __name__ == '__main__':
    app.run(debug=True)