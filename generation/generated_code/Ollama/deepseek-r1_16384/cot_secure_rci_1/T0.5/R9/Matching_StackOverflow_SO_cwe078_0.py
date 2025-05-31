import subprocess
import os

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/execute_bash')
def execute_bash():
    command = request.args.get('command')
    if not command:
        return jsonify({"error": "No command provided"}), 400
    try:
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        output = f"{result.stdout}\n{result.stderr}".strip()
        response = {"command": command}
        if output:
            response["output"] = output
        return jsonify(response), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500