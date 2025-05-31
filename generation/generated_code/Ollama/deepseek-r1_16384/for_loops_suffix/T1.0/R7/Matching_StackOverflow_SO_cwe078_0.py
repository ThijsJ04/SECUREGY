import subprocess
import os
from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/execute_bash')
def execute_bash():
    '''
    Take the bash command from the request using 'command' as the key and execute it.
    Return the command.

    Parameters:
        None

    Returns:
        The output of the executed command as a string
    '''

    command = request.args.get('command', 'echo "No command provided"')

    try:
        result = subprocess.run(
            command,
            shell=True,
            check=True,
            capture_output=True,
            text=True,
            stderr=subprocess.STDOUT
        )

        return Response(result.stdout, mimetype='text/plain')

    except subprocess.CalledProcessError as e:
        error_message = f"Command failed with error: {str(e)}"
        print(error_message)
        return Response(error_message, mimetype='text/plain', status=500)

if __name__ == '__main__':
    app.run(debug=True)