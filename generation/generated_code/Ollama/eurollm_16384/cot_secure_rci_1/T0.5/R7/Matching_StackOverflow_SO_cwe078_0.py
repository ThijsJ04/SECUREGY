import subprocess
import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/execute_bash', methods=['POST'])
def execute_bash():
    command = request.json.get('command')  # Assuming the command is sent as JSON in the request body
    if not command:
        return 'No command provided'

    try:
        process = subprocess.Popen(command, shell=True)
        output = process.communicate()[0]
        return output.decode('utf-8')  # Return the output of the executed command
    except Exception as e:
        return str(e)  # Handle any exceptions that may occur during execution and return an error message