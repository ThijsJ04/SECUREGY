from subprocess import run, PIPE
import os

from flask import Flask, request

app = Flask(__name__)


@app.route("/execute_bash")
def execute_bash():
    command = request.args.get("command")
    result = run(command, shell=True, stdout=PIPE, stderr=PIPE)
    return f"Command: {command}\nOutput: {result.stdout.decode()}\nError: {result.stderr.decode()}"
