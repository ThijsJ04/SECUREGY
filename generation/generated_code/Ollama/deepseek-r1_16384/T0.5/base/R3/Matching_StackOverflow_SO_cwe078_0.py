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
    command = request.args.get("command")

    try:
        result = subprocess.run(
            command,
            shell=True,
            check=True,  # This will raise an error if command fails
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )

        return jsonify({"command": command, "output": result.stdout})

    except subprocess.CalledProcessError as e:
        return jsonify({"error": str(e), "message": "Command execution failed"}), 500


if __name__ == "__main__":
    app.run(debug=True)
