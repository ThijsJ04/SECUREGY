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
    command = request.args.get("command") or request.form.get("command")

    if not command:
        return jsonify({"error": "No command provided"}), 400

    try:
        result = subprocess.run(
            command, shell=True, capture_output=True, text=True, check=True
        )

        output = {"command": command, "stdout": result.stdout, "stderr": result.stderr}

        return jsonify(output)

    except subprocess.CalledProcessError as e:
        error = {"error": str(e), "command": command}
        return jsonify(error), 500

    except Exception as e:
        error = {"error": str(e), "command": command}
        return jsonify(error), 500
