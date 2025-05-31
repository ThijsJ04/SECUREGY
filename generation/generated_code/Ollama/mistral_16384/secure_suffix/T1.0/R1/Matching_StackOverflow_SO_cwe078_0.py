from flask import Flask, request, jsonify
import subprocess, os

app = Flask(__name__)

@app.route('/execute_bash')
def execute_bash():
    command = request.args.get('command', '')
    result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE)
    return jsonify({'command': command, 'output': result.stdout.decode()})