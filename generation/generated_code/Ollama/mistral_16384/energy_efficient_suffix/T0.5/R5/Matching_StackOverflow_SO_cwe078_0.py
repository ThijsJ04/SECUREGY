from flask import Flask, request, jsonify
import subprocess, os

app = Flask(__name__)

@app.route('/execute_bash')
def execute_bash():
    command = request.args.get('command', default='')
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return jsonify({'command': command, 'result': result.stdout})