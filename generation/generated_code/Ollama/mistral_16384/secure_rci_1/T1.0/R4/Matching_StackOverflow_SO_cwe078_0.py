import subprocess, os
import flask

app = flask.Flask(__name__)

@app.route('/execute_bash')
def execute_bash():
    command = flask.request.args.get('command')
    result = subprocess.check_output(command, shell=True, universal_newlines=True)
    return f'Command: {command}\nResult: {result}'