from flask import Flask, request
import subprocess
import os

app = Flask(__name__)

@app.route('/execute_bash', methods=['POST'])
def execute_bash():
    command = request.form.get('command')  # Retrieve the Bash command from the request
    if not command:  # Check if the command is provided
        return 'Command is required.'

    # Execute the Bash command using subprocess.run
    try:
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
        output, error = process.communicate()  # Get output of executed command
        if error:
            return 'Error executing Bash command.' + str(error)
    except Exception as e:
        print(e)
        return 'Failed to execute the command.'

    # Return the output of the executed command
    return 'Command execution result:\n' + str(output)  # return the output