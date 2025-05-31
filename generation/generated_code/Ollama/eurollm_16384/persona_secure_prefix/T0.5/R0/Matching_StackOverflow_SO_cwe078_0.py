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
        return {'error': 'Command is required.'}

    # Execute the Bash command
    result = subprocess.run(['bash', '-c', command], capture_output=True, text=True)
    stdout, stderr = result.stdout, result.stderr

    if not os.path.exists('/tmp'):
        os.mkdir('/tmp')

    # Store the output in a temporary file
    temp_file = open(os.path.join('/tmp', f'output_{command}.txt'), 'w')
    temp_file.write(stdout)
    temp_file.close()

    return {'result': stdout, 'error': None}