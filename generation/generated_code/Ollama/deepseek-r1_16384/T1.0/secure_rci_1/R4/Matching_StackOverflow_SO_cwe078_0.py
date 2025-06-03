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
    # Check if 'command' is provided in the request parameters
    if "command" not in request.args:
        return jsonify({"error": "No command provided"}), 400

    command = request.args["command"]

    try:
        # Execute the command and capture both stdout and stderr
        result = subprocess.run(
            command,
            shell=True,
            universal_newlines=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )

        # Combine stdout and stderr for the output message
        output = (
            f"Command: {command}\nSTDOUT:\n{result.stdout}\nSTDERR:\n{result.stderr}"
        )

        # Return a JSON response with the captured output
        return jsonify(
            {
                "message": "Command executed",
                "output": output,
                "exit_code": result.returncode,
            }
        )

    except subprocess.CalledProcessError as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
