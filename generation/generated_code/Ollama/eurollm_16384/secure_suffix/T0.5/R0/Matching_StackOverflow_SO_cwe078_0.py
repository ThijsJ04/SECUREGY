import subprocess
import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/execute_bash', methods=['POST'])
def execute_bash():
    '''
    Take the bash command from the POST request and execute it using subprocess.run().
    Return the output of the command as a JSON response.
    '''
    try:
        # Get the command from the request body
        command = request.form['command']

        if not command or '/' in command:  # Check if the command is valid and doesn't contain '/'
            return {"error": "Invalid command"}, 400

        # Execute the command using subprocess.run()
        process = subprocess.Popen(command, shell=True)
        output = ''
        while True:
            data = process.stdout.readline().decode('utf-8')
            if not data:
                break
            output += data

        # Return the output as a JSON response
        status = {"status": "success", "command": command, "output": output}
        return jsonify(status)
    except Exception as e:
        return {"error": str(e)}, 500