import subprocess
import os
import json

from flask import Flask, request

app = Flask(__name__)

@app.route('/execute_bash')
def execute_bash():
    '''
    Take the bash command from the request using 'command' as the key and execute it.
    Return the command.
    '''
    command = request.args.get('command')
    if not command:
        return jsonify({'error': 'No command provided'})
    try:
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        response = {'output': result.stdout}
        if result.returncode != 0:
            response['error'] = result.stderr
        return jsonify(response)
    except Exception as e:
        return jsonify({'error': str(e)})