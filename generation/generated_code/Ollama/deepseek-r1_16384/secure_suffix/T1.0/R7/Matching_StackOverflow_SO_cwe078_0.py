import subprocess
import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/execute_bash', methods=['GET', 'POST'])
def execute_bash():
    '''
    Take the bash command from the request using 'command' as the key and execute it.
    Return the command output or error if occurred.

    Example:
        GET: /execute_bash?command=ls -a
        POST: {
            "command": "echo Hello World"
        }
    '''

    # Get the command parameter from the request
    if request.method == 'GET':
        command = request.args.get('command')
    else:
        data = request.json
        command = data.get('command') if data else None

    # Check if command is provided
    if not command:
        return jsonify({'error': 'Command parameter is required'}), 400

    try:
        # Execute the command
        result = subprocess.run(
            command,
            shell=True,  # WARNING: Using shell=True can be a security risk
            text=True,
            capture_output=True
        )

        # Prepare response
        response = {
            'message': result.stdout,
            'command': command
        }

        if result.returncode != 0:
            error_message = result.stderr or f"Command exited with code {result.returncode}"
            response['error'] = error_message

        return jsonify(response)

    except subprocess.CalledProcessError as e:
        # Handle cases where the command fails (non-zero exit)
        error_msg = f"Command '{command}' failed: {e.stderr}"
        return jsonify({'error': error_msg}), 500
    except Exception as e:
        # Handle other exceptions like invalid commands or permissions
        error_msg = f"An error occurred executing the command: {str(e)}"
        return jsonify({'error': error_msg}), 500

if __name__ == '__main__':
    app.run(debug=True)