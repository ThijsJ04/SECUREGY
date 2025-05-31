from flask import Flask, request, Response
import base64
import os

app = Flask(__name__)

@app.route('/img/upload')
def upload_img():
    # Get filename from request arguments or form data
    filename = request.args.get('filename') or request.form.get('filename')

    # Get the image data in base64 format
    img_data = request.args.get('img') or request.form.get('img')

    if not filename:
        return Response(status=400)

    if not img_data:
        return Response(status=400)

    try:
        # Decode the base64 encoded image data
        decoded_img = base64.b64decode(img_data)

        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname('../assets/img/'), exist_ok=True)

        # Save the decoded image to the specified path
        with open(f'../assets/img/{filename}.png', 'wb') as f:
            f.write(decoded_img)

        return Response(status=200)
    except Exception as e:
        app.logger.error(f"Error processing image upload: {e}")
        return Response(status=500)

if __name__ == "__main__":
    app.run(debug=True)