import subprocess, os
import flask

app = flask.Flask(__name__)


@app.route("/execute_bash")
def execute_bash():
    command = request.args.get("command")
    if not command:
        return "Error: command is required", 400

    try:
        result = subprocess.check_output(command, shell=True, universal_newlines=True)
    except Exception as e:
        return f"Error executing command: {str(e)}", 500

    return command + " -> " + result
