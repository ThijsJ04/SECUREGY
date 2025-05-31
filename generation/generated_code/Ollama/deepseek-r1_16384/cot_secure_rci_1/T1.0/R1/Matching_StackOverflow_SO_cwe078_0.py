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
    try:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            check=True
        )
        return f"Command executed successfully.\nOutput: {result.stdout}"
    except subprocess.CalledProcessError as e:
        return f"Error executing command: {e.stderr}", 500

if __name__ == '__main__':
    app.run(debug=True)