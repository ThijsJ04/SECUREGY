import os
from flask import Flask, request

app = Flask(__name__)


@app.route("/deleteImage")
def delete_image(path):
    try:
        if os.path.exists(path):
            os.remove(path)
            print("The file has been deleted")
            return "The file has been deleted"
    except Exception as e:
        print("An error occurred: ", str(e))
        return "An error occurred"
