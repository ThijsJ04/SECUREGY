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
    # Get the command parameter from query arguments or form data
    command = request.args.get('command') or request.form.get('command')

    # If no command is provided, return an error message
    if not command:
        return "Command parameter is required."

    try:
        # Execute the bash command using subprocess.run()
        subprocess.run(command, shell=True)
        # Return the executed command as a response
        return command
    except Exception as e:
        # If there's an exception during execution, return the error message
        return f"Error executing command: {str(e)}"