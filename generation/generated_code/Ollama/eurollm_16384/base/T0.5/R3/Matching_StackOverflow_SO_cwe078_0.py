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
    data = request.get_json()
    command = data.get('command')
    if not command:
        return {"error": "Missing command"}, 400

    try:
        process = subprocess.Popen(command, stdout=subprocess.PIPE)
        output, error = process.communicate()
        if error:
            return {"error": "Error executing command"}, 500
        else:
            return output.decode('utf-8')
    except subprocess.CalledProcessError as e:
        print(e)
        return {"error": f"Command '{command}' failed with exit code {e.returncode}"}, 500