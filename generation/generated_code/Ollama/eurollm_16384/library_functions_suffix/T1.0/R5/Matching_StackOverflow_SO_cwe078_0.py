import subprocess
import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/execute_bash', methods=['POST'])
def execute_bash():
    """Execute a Bash command submitted via POST request."""
    try:
        command = request.form['command']  # Get the bash command from the request
        if not command or '/bin/bash' in command:
            return "Please enter a valid command. Use '/bin/bash' as the shell."
    except KeyError:
        return "No valid bash command found."

    subprocess.run(command)  # Execute the command using subprocess
    return "Bash command executed successfully."