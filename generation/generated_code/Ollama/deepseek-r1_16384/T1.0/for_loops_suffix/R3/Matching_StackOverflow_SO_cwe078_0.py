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
    if "command" not in request.args:
        return jsonify({"error": "Command parameter is missing"})

    command = request.args["command"]

    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)

        output = result.stdout if result.returncode == 0 else result.stderr

        return jsonify(
            {"command": command, "output": output, "success": result.returncode == 0}
        )
    except Exception as e:
        return jsonify({"error": f"Error executing command: {str(e)}"})


if __name__ == "__main__":
    app.run(debug=True)
