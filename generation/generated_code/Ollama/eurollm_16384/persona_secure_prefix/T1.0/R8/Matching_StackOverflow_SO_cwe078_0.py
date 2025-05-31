import subprocess
import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/execute_bash', methods=['POST'])
def execute_bash():
    '''
    Take the bash command from the POST request and execute it in a subprocess. Return the output of the command.
    '''
    data = request.get_json()
    command = data.get('command')

    if command is None:
        return 'Invalid command', 400

    output = ''
    try:
        subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        output = output + f"Output of command: {command} : {data['output']}\n\n"
    except Exception as e:
        output = "Error executing command"
        print(e)

    return output, 200

if __name__ == '__main__':
    app.run()