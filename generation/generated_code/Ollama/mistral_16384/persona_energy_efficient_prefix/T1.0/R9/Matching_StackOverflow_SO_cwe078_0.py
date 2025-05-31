import subprocess, os, base64
from flask import Flask, request

app = Flask(__name__)

@app.route('/execute_bash')
def execute_bash():
    command = request.args.get('command')
    if not command:
        return "Error: 'command' parameter is required.", 400
    encoded_command = base64.b64encode(command.encode()).decode()
    output = subprocess.check_output(f"base64 -d {encoded_command}", shell=True, stderr=subprocess.STDOERR)
    result = os.system(output)
    return f'Command executed: {command}\nResult: {result}', 200