import subprocess
import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/execute_bash')
def execute_bash():
    '''
    Take the bash command from the request using 'command' as the key and execute it.
    Return the command.
    '''
    # Get the command parameter from the request
    command = request.args.get('command', '') or request.form.get('command', '')

    # Execute the bash command
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Combine stdout and stderr into a single output variable
    output = (result.stdout + result.stderr).decode()

    # Return the combined output as JSON response
    return jsonify({'output': output})