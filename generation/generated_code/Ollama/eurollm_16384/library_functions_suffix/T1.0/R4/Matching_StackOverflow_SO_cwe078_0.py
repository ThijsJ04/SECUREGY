import subprocess
import os
from flask import Flask, request

app = Flask(__name__)

# Create a dictionary of Bash commands to execute
bash_commands = {
    'ls': 'echo "Listing directory contents..."',
    'cat': 'echo "Printing file content..."',
}

@app.route('/execute_bash')
def execute_bash():
    command = request.args.get('command')
    if not command:
        return 'Error: No command provided.'

    # Check if the command is in the dictionary of Bash commands
    if command in bash_commands:
        subprocess.run(bash_commands[command])
    else:
        return 'Error: Unknown command.'

    return ''