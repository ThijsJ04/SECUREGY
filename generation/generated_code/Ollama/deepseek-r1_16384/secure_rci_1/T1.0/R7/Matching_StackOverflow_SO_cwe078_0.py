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
    try:
        command = request.args.get('command')
        if not command:
            raise ValueError("Command is required")
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return f"Command executed: {command}"
    except ValueError as e:
        return f"Error: {str(e)}", 400
    except subprocess.CalledProcessError as e:
        return f"Command failed: {str(e)}", 400