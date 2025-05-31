import subprocess
import os
from flask import request, jsonify

app = Flask(__name__)

@app.route('/execute_bash', methods=['POST'])
def execute_bash():
    command = request.json.get('command')
    if not command:
        return jsonify({"error": "No command provided"}), 400

    try:
        subprocess.check_call(command, shell=True)
        return jsonify({"result": "Command executed successfully"})
    except subprocess.CalledProcessError as e:
        return jsonify({"error": str(e), "exit_code": e.returncode}), 500