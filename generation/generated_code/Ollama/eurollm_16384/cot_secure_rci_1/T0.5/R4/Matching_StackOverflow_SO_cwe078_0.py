import subprocess
import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/execute_bash', defaults={'command': ''})
def execute_bash(command):
    '''
    Take the bash command from the request using 'command' as the key and execute it.
    Return the command.
    '''
    subprocess.check_call([command])  # Replace [command] with your actual command
    return "Command executed successfully."

if __name__ == '__main__':
    app.run(debug=True)