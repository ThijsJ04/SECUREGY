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
        return "No command specified"

    try:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True
        )

        response = f"Command executed: {command}\n"
        if result.stdout:
            response += f"Output:\n{result.stdout}"
        if result.stderr:
            response += f"Error:\n{result.stderr}"

        return response

    except FileNotFoundError:
        return f"Command not found: {command}"
    except Exception as e:
        return f"Error executing command: {str(e)}"

if __name__ == "__main__":
    app.run(debug=True)