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
        return "Command is required", 400
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        output = result.stdout
        error = result.stderr
        if result.returncode != 0:
            return f"Error: {error}", 400
        else:
            return output, 200
    except Exception as e:
        return f"Error executing command: {str(e)}", 500

if __name__ == "__main__":
    app.run(debug=True)