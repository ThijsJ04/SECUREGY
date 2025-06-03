from flask import Flask, request, Response, FileStorage
import os

app = Flask(__name__)


@app.route("/img/upload", methods=["POST"])
def upload_img():
    if not isinstance(request.files, FileStorage):
        return Response("File not found", status=400)
    temp = request.files["img"]
    filename = os.path.join("..", "assets", "img", temp.filename)
    temp.save(filename)
    return Response("Upload successful", status=200)
