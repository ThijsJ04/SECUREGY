import subprocess
import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/execute_bash', methods=['POST'])
def execute_bash():
    '''
    Take the bash command from the POST request and execute it using the subprocess module.
    Return the command.
    '''
    data = request.get_json()
    command = data.get('command')  # Extract the bash command from the JSON data

    if not command:
        return {'error': 'No command provided'}

    try:
        process = subprocess.Popen(command, stdout=subprocess.PIPE)
        output, error = process.communicate()

        if error:
            return {'error': f"Command execution failed: {error}"}

        return output
    except Exception as e:
        return {'error': str(e)}