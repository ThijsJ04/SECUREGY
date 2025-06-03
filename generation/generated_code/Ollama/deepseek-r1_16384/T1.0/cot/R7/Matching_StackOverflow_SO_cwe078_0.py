import subprocess
import os

from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/execute_bash")
def execute_bash():
    cmd = request.args.get("command")
    if not cmd:
        return jsonify({"error": "No command provided"})

    try:
        result = subprocess.run(cmd, shell=True, text=True, capture_output=True)
        if result.returncode == 0:
            return jsonify({"output": result.stdout})
        else:
            return jsonify({"error": result.stderr})
    except Exception as e:
        return jsonify({"error": str(e)})
