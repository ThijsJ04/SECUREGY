import subprocess
import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/execute_bash', methods=['POST'])
def execute_bash():
    try:
        # Get the bash command from the request using 'command' as the key
        command = request.form["command"]
    except KeyError:
        return "Error: No command provided", 400

    # Execute the bash command and return it
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    output, error = process.communicate()
    if output:
        return "Command executed successfully:\n" + str(output), 200
    else:
        return "Error executing command", 500