from flask import Flask, request, jsonify
import subprocess
import os

app = Flask(__name__)

@app.route('/execute_bash')
def execute_bash():
    command = request.args.get('command')
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return jsonify({'command': command, 'result': result.stdout})