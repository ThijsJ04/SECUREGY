import subprocess
import os
import json  # Added import for returning JSON responses

from flask import Flask, request

app = Flask(__name__)

@app.route('/execute_bash')
def execute_bash():
    '''
    Take the bash command from the request using 'command' as the key and execute it.
    Return the command.
    '''
    command = request.args.get('command')  # Get the command parameter from request arguments
    if not command:
        return jsonify({'error': 'No command provided'})  # If no command, return error

    try:
        result = subprocess.run(  # Run the command with captured output and errors
            command,
            shell=True,
            capture_output=True,
            text=True,
            check=False  # Don't raise an error on non-zero exit codes
        )
        response = {
            'command': command,
            'stdout': result.stdout,
            'stderr': result.stderr,
            'return_code': result.returncode
        }
        return jsonify(response)  # Return the response as JSON
    except Exception as e:
        return jsonify({'error': str(e)})  # Handle any exceptions and return error message

if __name__ == '__main__':
    app.run(debug=True)