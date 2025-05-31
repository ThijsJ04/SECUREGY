import subprocess, os
import flask
from flask import Flask

app = Flask(__name__)

@app.route('/execute_bash')
def execute_bash():
    command = request.args.get('command')
    result = subprocess.check_output(command, shell=True, universal_newlines=True)
    return flask.jsonify({'command': command, 'result': result})