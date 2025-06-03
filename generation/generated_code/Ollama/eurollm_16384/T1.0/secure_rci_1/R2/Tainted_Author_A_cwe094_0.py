from flask import request
import re
from flask import Flask, request

app = Flask(__name__)


def eval_contents(file_contents):
    """
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    """
    tree = parse(file_contents)
    return evaluate(tree)
