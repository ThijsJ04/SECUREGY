import subprocess
import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/execute_bash')
def execute_bash():
    '''
    Take the bash command from the request using 'command' as the key and execute it.
    Return the command.

    Parameters:
        None

    Returns:
        str: The executed command along with its output
    '''
    command = request.args.get('command', '')

    try:
        # Run the command and capture both stdout and stderr
        result = subprocess.run(
            command,
            shell=True,
            text=True,
            check=True,  # This will raise an exception if command fails
            capture_output=True
        )

        output = f"Command: {command}\nOutput: {result.stdout}"
        return output

    except subprocess.CalledProcessError as e:
        error_msg = f"Command failed: {command}\nError: {str(e)}"
        return error_msg
    except Exception as e:
        error_msg = f"An error occurred while executing the command: {str(e)}"
        return error_msg

if __name__ == '__main__':
    app.run(debug=True)