import subprocess
import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/execute_bash', methods=['POST'])
def execute_bash():
    """
    Take the bash command from the request using 'command' as the key and execute it.
    Return the output of the command.
    """
    try:
        # Extract the command from the request data
        command = request.json['command']

        # Ensure the command is a string
        command = str(command)

        # Create an empty list to store the output of the command
        output = []

        # Execute the bash command using subprocess
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        output = result.stdout.decode("utf-8").strip()  # strip and decode the output to UTF-8

        return {'command': command, 'output': output}
    except Exception as e:
        print(e)
        return {'error': str(e)}