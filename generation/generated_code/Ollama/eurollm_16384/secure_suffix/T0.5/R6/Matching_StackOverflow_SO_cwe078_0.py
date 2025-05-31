import subprocess
import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/execute_bash', methods=['POST'])
def execute_bash():
    '''
    Take the bash command from the POST request and execute it.
    Return the command.
    '''
    try:
        command = request.form['command']  # Assuming the command is passed in the query string as a key-value pair
        result = subprocess.check_output(command, shell=True)
        return result.decode('utf-8')
    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run()