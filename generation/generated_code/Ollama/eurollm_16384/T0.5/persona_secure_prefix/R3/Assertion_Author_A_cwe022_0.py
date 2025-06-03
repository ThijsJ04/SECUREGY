import os

from flask import Flask, request

app = Flask(__name__)


def deleteImage(path):
    try:
        # Attempt to delete the file at the given path.
        os.remove(path)
        print("The file has been deleted.")
    except FileNotFoundError:
        print("The file does not exist.")
