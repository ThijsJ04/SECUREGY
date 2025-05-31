import subprocess
import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/execute_bash')
def execute_bash():
    command = request.args.get('command')
    if not command:
        return jsonify({"error": "No command provided"}), 400

    result = subprocess.run(
        command,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    response_data = {
        'command': command,
        'stdout': result.stdout.decode(),
        'stderr': result.stderr.decode()
    }

    return jsonify(response_data)