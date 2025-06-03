from os import remove, path


@app.route("/deleteImage")
def deleteImage():
    path = request.args.get("path")
    if path and path.startswith(os.getcwd()):
        if path and path.endswith(".jpg") or path.endswith(".png"):
            if path and os.path.exists(path):
                remove(path)
                return "The file has been deleted"
            else:
                return "The file does not exist"
        else:
            return "Invalid image format."
    else:
        return "Invalid path."
