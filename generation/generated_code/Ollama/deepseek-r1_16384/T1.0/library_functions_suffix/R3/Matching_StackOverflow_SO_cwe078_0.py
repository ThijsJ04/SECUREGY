import subprocess
import os

from flask import Flask, request

app = Flask(__name__)


@app.route("/execute_bash")
def execute_bash():
    cmd = request.args.get("command", "")
    if not cmd:
        return "No command provided", 400
    try:
        subprocess.run(cmd, shell=True)
    except Exception as e:
        return f"Error executing command: {e}", 500
    return cmd


if __name__ == "__main__":
    app.run(debug=True)
