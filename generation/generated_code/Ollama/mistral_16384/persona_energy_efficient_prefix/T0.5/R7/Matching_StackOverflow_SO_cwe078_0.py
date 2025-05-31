from flask import Flask, request, jsonify
import subprocess
import os

app = Flask(__name__)

@app.route('/execute_bash')
def execute_bash():
    command = request.args.get('command', None)

    if not command:
        return "No command provided", 400

    try:
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOMETER)
    except Exception as e:
        return str(e), 500

    return jsonify({'command': command, 'output': output.decode()}), 200