from flask import Flask, request

app = Flask(__name__)


def contents_dict():
    eval("{" + file_contents + "}")  # Replace this line
    return eval(file_contents)
