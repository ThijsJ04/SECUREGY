from flask import Flask, request, Response
import base64

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "../assets/img/"
app.config["ALLOWED_EXTENSIONS"] = ["png", "jpg", "jpeg"]


def allowed_file(filename):
    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower() in app.config["ALLOWED_EXTENSIONS"]
    )


@app.route("/img/upload")
def upload_img():
    if request.method == "POST":
        if allowed_file(request.filename):
            filebytes = request.files["image"].read()
            print("Image file size: ", len(filebytes))
            with open(
                app.config["UPLOAD_FOLDER"] + "{}.png".format(request.form["filename"]),
                "wb",
            ) as f:
                f.write(filebytes)
            print("Image saved successfully!")
        else:
            return "Invalid file type", 403
    return "Error in uploading the image"
