import subprocess
import os

from flask import Flask, request, Response

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
            raise ValueError("Command parameter is required")

        # Execute the command
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            encoding='utf-8'
        )

        output = result.stdout
        error = result.stderr

        if error:
            return f"Error: {error}", 400

        return output

    except subprocess.CalledProcessError as e:
        return f"Command failed: {str(e)}", 400
    except Exception as e:
        return f"An error occurred: {str(e)}", 500

if __name__ == '__main__':
    app.run(debug=True)