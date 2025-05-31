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
    try:
        command = request.form.get('command', '')
        if not command:
            return json.dumps({'error': 'No command provided'})

        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True
        )

        output = result.stdout
        error = result.stderr

        response_data = {
            'command': command,
            'stdout': output,
            'stderr': error,
            'exit_code': result.returncode
        }

        return json.dumps(response_data)
    except subprocess.TimeoutError:
        return json.dumps({'error': 'Command timed out'})
    except Exception as e:
        return json.dumps({'error': str(e), 'command': command})