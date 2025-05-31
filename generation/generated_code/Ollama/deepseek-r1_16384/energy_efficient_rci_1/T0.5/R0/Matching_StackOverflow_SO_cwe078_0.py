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
    command = request.args.get('command')  # Get command parameter from query string
    if not command:
        return json.dumps({'error': 'No command provided'}), 400

    try:
        result = subprocess.run(
            command,
            shell=True,  # Execute the command in a shell
            check=True,  # Raise an error on non-zero exit status
            capture_output=True,  # Capture stdout and stderr
            text=True  # Return output as strings instead of bytes
        )

        response = {
            'command': command,
            'stdout': result.stdout,
            'stderr': result.stderr,
            'exit_code': result.returncode
        }

        return json.dumps(response)

    except subprocess.CalledProcessError as e:
        error_response = {
            'error': str(e),
            'command': command,
            'stderr': e.stderr.decode() if hasattr(e, 'stderr') else ''
        }
        return json.dumps(error_response), 500

    except Exception as e:
        error_response = {'error': str(e)}
        return json.dumps(error_response), 500