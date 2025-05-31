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

    if not filename or not img_data:
        return Response(status=400)

    try:
        # Decode the base64 string
        decoded_data = base64.b64decode(img_data)

        # Create directory if it doesn't exist
        os.makedirs("../assets/img", exist_ok=True)

        # Save the image to file
        filepath = f"../assets/img/{filename}.png"
        with open(filepath, 'wb') as f:
            f.write(decoded_data)

        return Response(status=200)
    except (ValueError, TypeError) as e:
        return Response(f"Invalid base64 data: {str(e)}", status=500)
    except IOError as e:
        return Response(f"Error saving file: {str(e)}", status=500)

if __name__ == "__main__":
    app.run(debug=True)