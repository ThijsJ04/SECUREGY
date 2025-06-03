import subprocess
import os
import json
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/execute_bash")
def execute_bash():
    command = request.args.get("command", "")
    if not command:
        return jsonify({"message": "No command provided"}), 400

    try:
        # Using shell=True allows for complex commands but is less secure
        process = subprocess.Popen(
            command,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )

        stdout, stderr = process.communicate()
        exit_code = process.poll()

        if exit_code == 0:
            return jsonify(
                {"message": "Command executed successfully", "output": stdout}
            ), 200
        else:
            error_message = f"Error executing command. Exit code: {exit_code}"
            if stderr:
                error_message += f". Details: {stderr}"
            return jsonify({"message": error_message}), 500

    except subprocess.CalledProcessError as e:
        return jsonify(
            {
                "message": f"Command failed with error: {str(e)}",
                "error_details": str(e.stderr),
            }
        ), 500
    except Exception as e:
        return jsonify({"message": f"System error occurred: {str(e)}"}), 500
