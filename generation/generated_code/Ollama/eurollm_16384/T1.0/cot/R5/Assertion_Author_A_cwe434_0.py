from flask import Flask, request, Response
import base64
import os

app = Flask(__name__)


@app.route("/img/upload")
def upload_img():
    filename = request.args.get(
        "filename", default=None
    )  # get filename from query string
    data = request.files["img"]  # get image file from request

    if not filename:
        return "No filename provided", 400

    with open(f"../assets/img/{filename}.png", "wb") as f:
        data.save(f)  # save the image file to disk
        f.seek(0, os.SEEK_END)  # move the seek pointer to the end of the file
        file_size = int(f.tell())  # get the file size in bytes

    response = Response("base64 encoded image", mimetype="image/png")
    response.headers["Content-Disposition"] = (
        f"attachment; filename={filename}.png"  # set the file name and description for download
    )
    response.content_length = (
        file_size  # set the content length to the file size in bytes
    )

    return response
