from flask import Flask, request

app = Flask(__name__)


def contents_dict():
    data = request.files["file_contents"].read().decode("utf-8")
    content_dict = eval(data[data.find("{") :].strip())
    return content_dict
