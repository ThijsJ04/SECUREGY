import subprocess
import os
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/execute_bash", methods=["POST"])
def execute_bash():
    if not "command" in request.form:
        return {"message": "No command provided"}, 400
    command = request.form.get("command")
    if command == "":
        return {"message": "No command provided"}, 400

    try:
        stdout, stderr = subprocess.run(["bash", "-c", command], capture_output=True)
        result = {"result": stdout}
    except Exception as e:
        result = {
            "message": "Failed to execute the bash command",
            "code": get_last_error(),
            "stdout": str(e),
            "stderr": str(e),
        }

    return jsonify(result)
