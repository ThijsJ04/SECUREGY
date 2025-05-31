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
    # Get the command from query parameters
    command = request.args.get('command', '')

    if not command:
        return "No command provided"

    try:
        result = subprocess.run(
            command,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        output = result.stdout
        error = result.stderr

        if output or error:
            return f"Command Output:\n{output}\nError:\n{error}" if error else f"{output}"
        else:
            return "Command executed successfully."

    except subprocess.CalledProcessError as e:
        return f"Error executing command: {str(e)}"

    except Exception as e:
        return f"An unexpected error occurred: {str(e)}"