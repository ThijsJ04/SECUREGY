import subprocess
import os

from flask import Flask, request

app = Flask(__name__)


def execute_bash():
    command = request.args.get("command")
    if command:
        os.system(command)
    return command
