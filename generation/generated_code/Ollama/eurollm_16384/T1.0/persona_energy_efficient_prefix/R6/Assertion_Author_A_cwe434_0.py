from werkzeug.datastructures import FileStorage
import os


@app.route("/img/upload")
def upload_img():
    if not request.files:
        return "No file part", 400

    file = request.files["img"]
    filename = secure_filename(file.filename)
    storage = FileStorage(file, save=os.path.join("..", "assets", "img", filename))
    storage.save()
    response = Response(content="Image uploaded successfully", status=200)
    return response
