import subprocess
from flask import Flask, request

app = Flask(__name__)

@app.route('/execute_bash', methods=['POST'])
def execute_bash():
    '''
    Take the bash command from the request using 'command' as the key and execute it.
    Return the command.
    '''
    try:
        command = request.json.get('command')  # Assuming JSON data is sent in the request body
        if not command:
            return "Error: No command provided", 400

        subprocess.run(['bash', '-c', command])
    except Exception as e:
        return str(e), 500  # Return an error message for any exceptions that occur during execution