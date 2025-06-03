from os import remove, path


@app.route("/deleteImage")
def deleteImage():
    path = request.args.get("path")
    if not path or not path.strip():
        return "Missing path parameter"

    file_path = os.path.join(os.getcwd(), path)

    if path and os.path.exists(file_path):
        os.remove(file_path)
        return "The file has been deleted"
    else:
        return "The file does not exist"
