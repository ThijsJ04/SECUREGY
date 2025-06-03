from flask import Flask, request, jsonify
import subprocess, os, json

app = Flask(__name__)


@app.route("/execute_bash")
def execute_bash():
    command = request.args.get("command")
    if not command:
        return jsonify({"error": "No command provided"}), 400

    try:
        result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOERR)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    return jsonify({"command": command, "result": result.decode("utf-8")})
