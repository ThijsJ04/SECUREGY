import subprocess
import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/execute_bash')
def execute_bash():
    '''
    Take the bash command from the request using 'command' as the key and execute it.
    Return the command.

    Example:
        Request: /execute_bash?command=ls
        Response: "Command: ls\nOutput: ['file1', 'file2']\n"
    '''

    # Get the command parameter from the request
    command = request.args.get('command')

    if not command:
        return "Error: No command provided", 400

    try:
        # Execute the bash command safely using subprocess
        result = subprocess.run(
            command,
            shell=True,
            check=True,  # This will raise an error if command fails
            capture_output=True,  # Capture both stdout and stderr
            text=True,  # Return output as string instead of bytes
            encoding='utf-8'
        )

        return f"Command: {command}\nOutput: {result.stdout}\nError: {result.stderr}\n"

    except subprocess.CalledProcessError as e:
        return f"Error executing command: {e}", 500

# Example usage:
# Visit http://localhost:5000/execute_bash?command=ls in your browser