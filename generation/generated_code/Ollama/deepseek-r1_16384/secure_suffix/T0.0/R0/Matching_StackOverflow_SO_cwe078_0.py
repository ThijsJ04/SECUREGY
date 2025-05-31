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
    command = request.args.get('command', '')

    try:
        # Use subprocess to safely execute the command
        result = subprocess.run(
            command,
            shell=True,  # Using shell is generally not recommended but required for complex commands
            capture_output=True,
            text=True,
            encoding='utf-8'
        )

        response = {
            'command': command,
            'stdout': result.stdout,
            'stderr': result.stderr,
            'return_code': result.returncode
        }

        return jsonify(response)

    except subprocess.CalledProcessError as e:
        return jsonify({'error': str(e)}), 500

    except Exception as e:
        return jsonify({'error': 'An unexpected error occurred'}), 500

if __name__ == '__main__':
    app.run(debug=True)