import subprocess
import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/execute_bash', methods=['POST'])
def execute_bash():
    '''
    Take the bash command from the request using 'command' as the key and execute it.
    Return the command.
    '''
    command = request.form.get('command')
    if not command:
        return 'Command is empty', 400

    result = subprocess.check_output(command, shell=True).decode("utf-8").strip()

    return f'Bash command executed:\n{result}', 200

if __name__ == '__main__':
    app.run(debug=True)