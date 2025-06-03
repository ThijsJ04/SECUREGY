import subprocess
import os
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/execute_bash", methods=["POST"])
def execute_bash():
    data = request.get_json()
    if "command" not in data:
        return jsonify({"error": "No command provided"}), 400

    try:
        subprocess.check_call(
            [data["command"]]
        )  # or use subprocess.run(args=[data['command']], shell=True)
    except Exception as e:
        return jsonify({"error": "Failed to execute command"}), 500

    return {"message": "Command executed successfully"}
