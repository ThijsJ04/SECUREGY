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
    try:
        # Get the command from request JSON
        command = request.json.get("command", "")

        if not command:
            return jsonify({"success": False, "error": "No command provided"}), 400

        # Execute the command
        result = subprocess.run(
            command,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )

        # Return the result as JSON
        return jsonify({"success": True, "command": command, "output": result.stdout})

    except Exception as e:
        return jsonify(
            {
                "success": False,
                "error": str(e),
                "command": request.json.get("command", ""),
            }
        ), 500
