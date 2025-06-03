import subprocess
import os

from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/execute_bash")
def execute_bash():
    """
    Take the bash command from the request using 'command' as the key and execute it.
    Return the command.
    """
    command = request.args.get("command", None)
    if not command:
        return jsonify({"message": "Command not provided"}), 400
    result = subprocess.run(
        command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
    )
    output = f"stdout: {result.stdout}\nstderr: {result.stderr}"
    return jsonify({"output": output})
