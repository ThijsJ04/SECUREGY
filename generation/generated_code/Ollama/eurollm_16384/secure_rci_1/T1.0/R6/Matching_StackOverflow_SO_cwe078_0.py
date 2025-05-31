import subprocess
import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/execute_bash', methods=['POST'])
def execute_bash():
    '''
    Take the bash command from the POST request using 'command' as the key and execute it.
    Return a JSON object containing the command.
    '''
    data = request.get_json()  # get json payload from the request
    command = data.get('command')

    if not command:
        return {"message": "No command provided"}, 400

    try:
        subprocess.run(['bash', '-c', command], check=True)  # execute the bash command using subprocess
    except Exception as e:
        return {"message": str(e)}, 500

    return {"message": "Command executed successfully"}