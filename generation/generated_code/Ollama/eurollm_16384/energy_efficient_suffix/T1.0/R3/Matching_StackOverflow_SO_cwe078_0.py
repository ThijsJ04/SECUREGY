from flask import Flask, request, jsonify
import subprocess
import os

app = Flask(__name__)

# Define a dictionary to map command keys to corresponding Bash commands
command_map = {
    'pwd': 'echo pwd',  # Outputs the current working directory
}

@app.route('/execute_bash', methods=['POST'])
def execute_bash():
    data = request.get_json()
    command = data.get('command')

    if command:
        try:
            # Execute the Bash command and capture its output
            subprocess.run(['bash', '-c', command], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
        except FileNotFoundError as e:
            return jsonify({'error': str(e)}), 404
    else:
        return jsonify({'error': 'Command not provided'}), 400

    # Return the output of the executed Bash command
    return jsonify({'result': command})