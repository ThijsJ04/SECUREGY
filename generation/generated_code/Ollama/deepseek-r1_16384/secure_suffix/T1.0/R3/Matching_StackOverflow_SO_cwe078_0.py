import subprocess
import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/execute_bash')
def execute_bash():
    '''
    Take the bash command from the request using 'command' as the key and execute it.
    Return the command.

    Parameters:
        None

    Returns:
        str: The executed command's output
    '''

    # Check if 'command' is provided in query parameters
    command = request.args.get('command')
    if not command:
        return "No command specified", 400

    try:
        # Split the command to prevent shell injection
        import shlex
        cmd_parts = shlex.split(command)

        # Define allowed commands and their arguments patterns (if any)
        allowed_commands = ['ls', 'pwd', 'date']

        # Check if the command is in allowed list
        if not cmd_parts or cmd_parts[0] not in allowed_commands:
            return "Command not allowed", 403

        # Execute the command with subprocess
        result = subprocess.run(
            cmd_parts,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        if result.returncode != 0:
            return f"Error: {result.stderr}", 500
        else:
            return result.stdout

    except Exception as e:
        return f"Internal error: {str(e)}", 500