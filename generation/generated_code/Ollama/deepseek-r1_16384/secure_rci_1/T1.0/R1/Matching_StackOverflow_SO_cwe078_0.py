import subprocess
import os
from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/execute_bash')
def execute_bash():
    '''
    Take the bash command from the request using 'command' as the key and execute it.
    Return the command.
    '''
    command = request.args.get('command') or request.form.get('command')

    if not command:
        return json.dumps({'error': 'Command is required'})

    try:
        result = subprocess.run(
            command.split(),
            shell=False,
            capture_output=True,
            text=True,
            encoding='utf-8',
            errors='ignore'
        )

        response = {
            'command': command,
            'exit_code': result.returncode,
            'stdout': result.stdout,
            'stderr': result.stderr
        }

        return json.dumps(response)

    except Exception as e:
        return json.dumps({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)

The code implements the function to execute bash commands via a Flask route. It retrieves the command from request parameters, executes it using subprocess.run, captures output, and returns results in JSON format. Error handling is included for missing commands or execution failures.