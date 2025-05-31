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
    # Get filename and img parameters
    filename = request.args.get('filename')
    img_data = request.args.get('img')

    try:
        if not filename or not img_data:
            return Response(status=400)

        # Decode base64 data
        decoded_image = base64.b64decode(img_data)

        # Save image to file
        save_path = f'../assets/img/{filename.replace(" ", "_")}.png'
        with open(save_path, 'wb') as f:
            f.write(decoded_image)

        return Response(status=200)
    except Exception as e:
        print(f"Error saving image: {e}")
        return Response(status=500)