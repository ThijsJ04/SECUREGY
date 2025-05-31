import subprocess
import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/execute_bash', methods=['POST'])
def execute_bash():
    command = request.form.get('command')
    if not command:
        return 'Command is required!'

    # Execute the Bash command using subprocess
    try:
        subprocess.check_call([command], shell=True)
        return f'Bash command {command} executed successfully.'
    except subprocess.CalledProcessError as e:
        return f'Bash command execution failed with error code {e}.'