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
    command = request.args.get('command')
    if not command:
        return "Command parameter is required", 400

    try:
        # Use subprocess to safely execute the command
        result = subprocess.run(
            command,
            shell=True,  # Using shell=True can be dangerous without proper validation
            capture_output=True,
            text=True,
            check=False
        )

        if result.returncode == 0:
            return f"Command executed successfully:\n{result.stdout}"
        else:
            return f"Error executing command:\n{result.stderr}", 500

    except Exception as e:
        return f"An error occurred: {str(e)}", 500

if __name__ == '__main__':
    app.run(debug=True)