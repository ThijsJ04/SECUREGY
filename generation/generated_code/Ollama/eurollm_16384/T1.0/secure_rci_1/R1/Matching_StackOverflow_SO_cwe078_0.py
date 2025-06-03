import subprocess
import os

from flask import Flask, request

app = Flask(__name__)


@app.route("/execute_bash", methods=["GET"])
def execute_bash():
    params = request.args  # Get the Bash command from the query string
    return "{0}".format(subprocess.check_output("echo {0}; date".format(params)))
