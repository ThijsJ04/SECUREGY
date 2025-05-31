import subprocess
import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/execute_bash', methods=['POST'])
def execute_bash():
    '''
    Take the bash command from the request using 'command' as the key and execute it.
    Return the command.
    '''
    data = request.get_json()  # Assuming JSON data is sent in the request body

    if not data or 'command' not in data:
        return "Error: Missing required field 'command'"

    command = data['command']

    if os.name == 'nt':  # Windows
        process = subprocess.Popen(command, shell=True)
    else:  # Unix/Linux
        process = subprocess.Popen(command, stdout=subprocess.PIPE)

    stdout, stderr = process.communicate()

    if stderr:
        return f"Error executing command: {stderr}"
    else:
        return f"Command executed: {stdout.decode('utf-8')}"