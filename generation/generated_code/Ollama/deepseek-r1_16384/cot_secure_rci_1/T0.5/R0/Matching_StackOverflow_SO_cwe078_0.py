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
        return "No command provided", 400
    try:
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE, text=True)
        output = f"Command executed:\n{result.stdout}\n\nError:\n{result.stderr}"
        if result.returncode != 0:
            output += f"\nReturn code: {result.returncode}"
        return output
    except Exception as e:
        return f"Exception occurred: {str(e)}", 500