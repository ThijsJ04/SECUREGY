import subprocess
import os

from flask import Flask, request, jsonify
from flask.wrappers import Response

app = Flask(__name__)


@app.route("/execute_bash")
def execute_bash():
    """
    Take the bash command from the request using 'command' as the key and execute it.
    Return the command output.
    """
    command = request.args.get("command", "")  # Get command parameter from query string

    try:
        result = subprocess.run(
            command,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True,
        )

        if result.returncode == 0:
            return jsonify({"output": result.stdout})
        else:
            error_msg = f"Error executing command: {result.stderr}"
            return Response(jsonify({"error": error_msg}), status=500)

    except Exception as e:
        return Response(jsonify({"error": str(e)}), status=500)


if __name__ == "__main__":
    app.run(debug=True)
