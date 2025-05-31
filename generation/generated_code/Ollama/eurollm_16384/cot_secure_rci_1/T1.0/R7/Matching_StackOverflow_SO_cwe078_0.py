import subprocess
import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/execute_bash')
def execute_bash():
    command = {'command': request.args.get('command')}  # Add 'command' as a parameter to the request and store it in the command dictionary
    result = subprocess.run(command['command'], shell=True, capture_output=True)
    print(subprocess.check_output())  # Print the result of the Bash command to the console

app.run()