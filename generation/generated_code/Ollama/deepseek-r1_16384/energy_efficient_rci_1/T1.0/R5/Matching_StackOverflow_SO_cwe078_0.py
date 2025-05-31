import subprocess
import os
from flask import Flask, request, jsonify

app = Flask(__name__)

def execute_command(command):
    try:
        process = subprocess.run(
            command,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        output = process.stdout if process.returncode == 0 else None
        error = process.stderr if process.returncode != 0 else None
        return {'command': command, 'output': output, 'error': error}
    except Exception as e:
        return {'command': command, 'error': str(e)}

@app.route('/execute_bash')
def execute_bash():
    command = request.args.get('command', '')
    if not command:
        return jsonify({'error': 'No command provided'}), 400
    result = execute_command(command)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)