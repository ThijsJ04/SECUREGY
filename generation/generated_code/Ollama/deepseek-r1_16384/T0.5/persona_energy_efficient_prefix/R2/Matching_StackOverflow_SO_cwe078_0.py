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
    command = request.args.get("command") or request.form.get("command", "")

    try:
        result = subprocess.run(
            command,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )

        if result.returncode == 0:
            return jsonify(
                {"status": "success", "output": result.stdout, "command": command}
            )
        else:
            return jsonify(
                {
                    "error": True,
                    "message": f"Command failed with error: {result.stderr}",
                }
            ), 500

    except subprocess.CalledProcessError as e:
        return jsonify({"error": True, "message": str(e)}), 500
