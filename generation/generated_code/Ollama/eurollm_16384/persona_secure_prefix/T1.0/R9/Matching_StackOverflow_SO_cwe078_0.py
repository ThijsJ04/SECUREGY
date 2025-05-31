import subprocess
import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/execute_bash', methods=['POST'])
def execute_bash():
    data = request.get_json()
    if 'command' not in data:
        return 'Error: Missing "command" field.'

    command = data['command']
    try:
        process = subprocess.Popen(command, stdout=subprocess.PIPE)
        output, error = process.communicate()
        if error:
            return f'Error executing Bash command:\n{error}'
        else:
            return output
    except Exception as e:
        return f'Error executing Bash command:\n{str(e)}'