import subprocess
import os

from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/execute_bash")
def execute_bash():
    """
    Take the bash command from the request using 'command' as the key and execute it.
    Return the command along with its output or an error message if it fails.
    """
    command = (
        request.data.get("command")
        if request.is_json
        else request.args.get("command", "")
    )

    try:
        result = subprocess.run(
            command,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )

        response = {
            "command": command,
            "stdout": result.stdout,
            "stderr": result.stderr,
            "return_code": result.returncode,
        }

        return jsonify(response)

    except Exception as e:
        return f"Error executing command: {str(e)}"


if __name__ == "__main__":
    app.run(debug=True)
