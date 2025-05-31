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
        cmd = request.args.get('command', '')
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)

        if result.returncode == 0:
            return f"Command executed successfully:\n{result.stdout}"
        else:
            return f"Error executing command:\n{result.stderr}", 500

    except Exception as e:
        return f"Exception occurred: {str(e)}", 500