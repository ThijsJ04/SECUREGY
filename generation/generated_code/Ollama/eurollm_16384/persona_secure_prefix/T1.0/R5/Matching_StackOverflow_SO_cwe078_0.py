import subprocess as sp
import os
from flask import Flask, request

app = Flask(__name__)

commands = {'command1': '# command to be executed', 
            'command2': '# another command'}

@app.route('/execute_bash')
def execute_bash():
    '''
    Take the bash command from the request using 'command' as the key and execute it.
    Return the command.
    '''
    command = request.args.get('command')
    if command:
        result = sp.run(['bash', '-c', commands[command]], check=True, shell=True)
        return str(result.stdout)[:-1]  # remove newline character from stdout
    else:
        return 'Invalid command'