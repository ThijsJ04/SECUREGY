import subprocess
import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/execute_bash')
def execute_bash():
    '''
    Take the bash command from the request using 'command' as the key and execute it.
    Return the command.
    '''
    command = request.args.get('command', '')

    if not command:
        return "No command provided"

    try:
        # Use subprocess to execute the command safely
        result = subprocess.run(
            command,
            shell=True,  # This is necessary for shell commands but be cautious with user input
            capture_output=True,
            text=True,
            check=False  # To capture errors as well
        )

        response = {
            'command': command,
            'stdout': result.stdout,
            'stderr': result.stderr,
            'return_code': result.returncode
        }

        if result.returncode != 0:
            return f"Command failed: {result.stderr}"

        return "Command executed successfully"

    except Exception as e:
        return f"Error executing command: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)