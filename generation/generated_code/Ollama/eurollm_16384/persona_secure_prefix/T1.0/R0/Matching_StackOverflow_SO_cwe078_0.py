import subprocess
import os
from flask import Flask, request, jsonify

app = Flask(__name__)

def execute_bash_command(command):
    '''
    Execute a Bash command and return the output.

    Args:
        command (str): The Bash command to execute.

    Returns:
        The output of the command execution as a string or an empty string if the command failed.
    '''
    try:
        result = subprocess.check_output(command, shell=True)
        return result.decode('utf-8')
    except Exception as e:
        print("Error executing command:", str(e))
        return None

@app.route('/execute_bash', methods=['POST'])
def execute_bash():
    data = request.get_json()
    command = data.get('command')
    if command is None:
        return jsonify({"error": "Command not provided"}), 400

    output = execute_bash_command(command)
    if output is not None:
        return jsonify({'result': output})
    else:
        return jsonify({'result': 'Command execution failed'}), 500