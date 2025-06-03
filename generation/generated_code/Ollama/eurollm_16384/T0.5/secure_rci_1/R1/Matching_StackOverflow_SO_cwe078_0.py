import subprocess
import os
from flask import Flask, request

app = Flask(__name__)


@app.route("/execute_bash", methods=["GET"])
def execute_bash():
    command = request.args.get("command")
    if command:
        output = subprocess.check_output(command, shell=True).decode()
        return f"Bash command executed successfully: {output}"
    else:
        return "No command provided."


@app.route("/execute_bash", methods=["POST"])
def execute_bash():
    command = request.form.get("command")
    if command:
        subprocess.check_call(command, shell=True)
        return "Bash command executed successfully."
    else:
        return "No command provided."


if __name__ == "__main__":
    app.run(debug=True)
