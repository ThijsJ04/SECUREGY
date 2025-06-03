import os

from flask import Flask, request

app = Flask(__name__)


def deleteImage(path):
    """
    This function is the Flask route for deleting an image. It takes a request URL path as input. The path should be of type string.

    It uses os.remove() to delete the file, checking if it exists with os.path.exists(). If the file does not exist, 'not found' is printed to indicate that.

    If you wish to raise an exception instead of printing a message, use try/except block here and return 'The operation has failed'.
    """
