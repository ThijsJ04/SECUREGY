import subprocess
import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/execute_bash')
def execute_bash():
    command = request.args.get('command') or request.form.get('command', '')
    if not command:
        return jsonify({'error': 'No command provided'})
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        output = result.stdout
        error = result.stderr
        if result.returncode != 0:
            raise subprocess.CalledProcessError(result.returncode, command, output=error)
        return jsonify({'output': output})
    except subprocess.CalledProcessError as e:
        return jsonify({'error': f'Command {command} failed with code {e.returncode}: {e.output}'})