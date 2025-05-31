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
    command = request.form.get('command')  # Get the command from the form data

    if not command:
        return "Command is required"

    try:
        subprocess.run(['bash', '-c', command], check=True)
        return f"Bash command executed successfully: {command}"
    except Exception as e:
        return f"Error executing Bash command: {e}"