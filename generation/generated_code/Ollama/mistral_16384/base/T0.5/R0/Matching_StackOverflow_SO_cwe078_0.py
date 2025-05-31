from flask import Flask, request, jsonify
import subprocess
import os

app = Flask(__name__)

@app.route('/execute_bash')
def execute_bash():
    command = request.args.get('command', None)
    if not command:
        return "No command provided", 400

    result = subprocess.run(command, shell=True, stdout=subprocess.TEXT_OUTPUT_STREAM)
    return jsonify({'command': command, 'result': result.stdout})