import subprocess
import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/execute_bash')
def execute_bash():
    command = request.args.get('command')
    result = subprocess.run(command, shell=True, capture_output=True)
    return {'command': command, 'result': result.stdout.decode('utf-8')}