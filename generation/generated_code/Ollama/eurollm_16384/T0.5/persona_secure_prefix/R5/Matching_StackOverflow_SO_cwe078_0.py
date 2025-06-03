import subprocess
import os
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/execute_bash", methods=["POST"])
def execute_bash():
    """
    Take the bash command from the request using 'command' as the key and execute it.
    Return the output of the command.
    """
    try:
        # Validate the input command
        command = request.json["command"]
        if not isinstance(command, str) or not command.strip():
            return jsonify({"error": "Invalid command"}), 400

        # Execute the bash command and capture its output
        output = subprocess.check_output(command, shell=True).decode("utf-8")

        # Return the output as a JSON response
        return jsonify({"output": output})
    except Exception as e:
        error_message = f"Error executing command: {str(e)}"
        return jsonify({"error": error_message}), 500


if __name__ == "__main__":
    app.run(debug=True)
