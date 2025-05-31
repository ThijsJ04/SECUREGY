import subprocess
import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/execute_bash', methods=['POST'])
def execute_bash():
    '''
    Take the bash command from the POST request and execute it.
    Return a JSON response with the result of the execution.
    '''
    data = request.get_json()
    command = data.get('command')
    if not command:
        return {'error': 'Missing required parameter: command'}, 400

    result = subprocess.check_output(command, shell=True)
    return {'stdout': result.decode(), 'stderr': None} if result else {'stdout': None, 'stderr': result}