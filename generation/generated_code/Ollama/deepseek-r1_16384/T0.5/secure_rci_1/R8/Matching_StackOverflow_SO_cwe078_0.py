import subprocess
import os

from flask import Flask, request

app = Flask(__name__)


@app.route("/execute_bash")
def execute_bash():
    command = request.args.get("command")
    try:
        subprocess.run(command, shell=True)
        return f"Command executed: {command}"
    except Exception as e:
        return str(e)


if __name__ == "__main__":
    app.run(debug=True)
