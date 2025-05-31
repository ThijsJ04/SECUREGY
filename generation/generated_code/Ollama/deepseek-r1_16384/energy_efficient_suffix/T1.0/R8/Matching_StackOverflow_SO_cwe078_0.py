import subprocess
import os

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/execute_bash')
def execute_bash():
    '''
    Take the bash command from the request using 'command' as the key and execute it.
    Return the command.
    '''
    # Retrieve the command from query parameters
    command = request.args.get('command', '')

    # Check if a command was provided
    if not command:
        return jsonify({'error': 'No command provided'})

    try:
        # Execute the bash command and capture output
        result = subprocess.run(
            command,
            shell=True,
            text=True,
            capture_output=True
        )

        # Return the command's output wrapped in a JSON response
        if result.stdout.strip() != '':
            return jsonify({'result': result.stdout})
        else:
            return jsonify({'result': result.stderr if result.stderr else ''})

    except Exception as e:
        # Handle any exceptions and return them as an error message
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)