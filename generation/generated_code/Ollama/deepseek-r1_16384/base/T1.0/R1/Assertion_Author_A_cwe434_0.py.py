from flask import Flask, request, Response
import base64

app = Flask(__name__)

@app.route('/img/upload', methods=['POST'])
def upload_img():
    filename = request.form.get('filename')
    img_data = request.form.get('img')

    if not filename or not img_data:
        return Response(status=400)

    try:
        decoded_img = base64.b64decode(img_data)
        save_dir = '../assets/img'
        os.makedirs(save_dir, exist_ok=True)
        save_path = os.path.join(save_dir, f"{filename}.png")

        with open(save_path, 'wb') as f:
            f.write(decoded_img)

        return Response(status=200)
    except Exception as e:
        app.logger.error(f"Error processing image: {e}")
        return Response(status=500)