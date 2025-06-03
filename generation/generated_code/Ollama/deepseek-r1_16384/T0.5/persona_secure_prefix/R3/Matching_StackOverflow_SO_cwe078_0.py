import subprocess
import os

from flask import Flask, request

app = Flask(__name__)


@app.route("/execute_bash")
def execute_bash():
    command = request.args.get("command", "")
    if not command:
        return "No command provided"
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        output = result.stdout
        error = result.stderr
        if output:
            return output
        elif error:
            return f"Error: {error}"
        else:
            return "Command executed successfully"
    except Exception as e:
        return f"Error executing command: {str(e)}"


if __name__ == "__main__":
    app.run(debug=True)
