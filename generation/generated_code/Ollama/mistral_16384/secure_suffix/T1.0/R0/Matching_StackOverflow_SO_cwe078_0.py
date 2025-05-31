import subprocess
import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/execute_bash')
def execute_bash():
    command = request.args.get('command', default='echo "Not provided"')
    result = subprocess.run(command, shell=True, stdout=subprocess.TEXT, stderr=subprocess.STDOUM)
    return result.stdout