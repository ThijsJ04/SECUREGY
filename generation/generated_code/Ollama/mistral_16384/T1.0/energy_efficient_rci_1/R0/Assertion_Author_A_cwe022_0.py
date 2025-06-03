from flask import Flask, request, abort

app = Flask(__name__)


@app.route("/deleteImage")
def deleteImage():
    path = request.args.get("path", None)
    if not path:
        abort(400, description="Path parameter 'path' is required.")
    if not os.path.exists(path):
        return "The file does not exist"
    os.remove(path)
    return "The file has been deleted"
