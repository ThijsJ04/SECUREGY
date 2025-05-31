import subprocess
import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/execute_bash', methods=['POST'])
def execute_bash():
    '''
    Take the bash command from the POST request and execute it. Return the command.
    '''
    command = request.json.get('command')  # Retrieve the command from the request body as JSON

    if command:  # Check if the command is not empty
        output = subprocess.check_output(command, shell=True)  # Execute the command using a shell
        print(output)  # Print the output for verification

        return {'output': output}  # Return the output of the executed command as JSON
    else:
        return 'Invalid input. Please provide a valid bash command.'  # Return an error message if no command is provided