from flask import Flask, request, Response
import base64
from werkzeug.utils import secure_filename
from PIL import Image

app = Flask(__name__)
UPLOAD_FOLDER = "./uploads/"
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}


def allowed_file(filename):
    """Check if the file extension is valid."""
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/img/upload")
def upload_img():
    """Handle image file uploads."""
    if "file" not in request.files:
        return Response(status=400, response="No file part")
    file = request.files["file"]
    if file.filename == "":
        return Response(status=400, response="No selected file")
    if allowed_file(file.filename):
        _, filename = os.path.split(file.filename)
        secure_filename = secure_filename(file.filename)
        file.save(os.path.join(UPLOAD_FOLDER, secure_filename))
        image = Image.open(os.path.join(UPLOAD_FOLDER, secure_filename))
        data = base64.b64encode(image.tobytes()).decode("utf-8")
        return Response(response=data, status=200, mimetype="image/png")
    else:
        return Response(status=400, response="Invalid file type")
