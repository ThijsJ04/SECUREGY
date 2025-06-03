from flask import Flask, request, Response
import base64
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = (
    "../assets/img"  # Change this to your local path if needed
)
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/img/upload")
def upload_img():
    if request.method == "POST":
        if "file" not in request.files:
            return {"message": "No file part"}
        file = request.files["file"]
        filename = file.filename
        allowed_extensions = ALLOWED_EXTENSIONS

        if file and allowed_file(filename):
            print("Allowed file type")
            original_img_data = base64.b64decode(
                request.files["file"].read()
            )  # get the original image data from "img" parameter
            # (use `request.files['file']` instead of `request['img']`)
            new_filename = filename.split(".")[-1] + ".png"
            destination = os.path.join(app.config["UPLOAD_FOLDER"], new_filename)
            with open(destination, "wb") as f:
                f.write(original_img_data)  # save the image to the file
            print("Saved Image Successfully")
            return {"message": "Image uploaded successfully."}
        else:
            return {"message": "Invalid file type or no file found."}

    else:
        return {"message": "Only POST request is allowed"}
