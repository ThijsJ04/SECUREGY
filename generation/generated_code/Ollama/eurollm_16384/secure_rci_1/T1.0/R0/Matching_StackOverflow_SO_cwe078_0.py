import subprocess
import os

from flask import Flask, request

app = Flask(__name__)

# Define a dictionary to store the bash command and its corresponding key
bash_command_dict = {
    'ls': 'ls -la',  # Use ls with optional arguments in quotes if needed
    'mkdir': 'mkdir -p directory_name',  # Use mkdir with required arguments in quotes
    'rm': 'rm file_name',  # Use rm with optional arguments in quotes if needed
}

@app.route('/execute_bash')
def execute_bash():
    command = request.args.get('command')
    if not command:
        return 'No command provided'

    if command in bash_command_dict:
        subprocess.run(['bash', '-c', f'"{bash_command_dict[command]}"']).check_output()
        return f'Command executed successfully: {bash_command_dict[command]}'
    else:
        return 'Invalid command. Please use one of the following commands: ls, mkdir, rm'