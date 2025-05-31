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
        return "No command provided", 400
    try:
        result = subprocess.run(command, shell=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = result.stdout + result.stderr
        if not output.strip():
            return 'Command executed successfully.'
        else:
            return output
    except Exception as e:
        return f"Error executing command: {str(e)}", 500