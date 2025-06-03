from os import remove, path


@app.route("/deleteImage")
def deleteImage():
    path_from_request = request.args.get("path", None)
    if not path_from_request or not path.isfile(os.path.join(".", path_from_request)):
        return "The file does not exist"

    try:
        remove(os.path.join(".", path_from_request))
        return "The file has been deleted"
    except Exception as e:
        return f"An error occurred while deleting the file: {str(e)}"
