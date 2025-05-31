import subprocess
import os
from flask import request

app = Flask(__name__)

@app.route('/execute_bash', methods=['POST'])
def execute_bash():
    data = request.get_json()
    if not 'command' in data:
        return {"error": "Missing required parameter: command"}, 400

    command = data['command']
    try:
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        output, error = process.communicate()
        if output is None or error is None:
            return {"output": "No output from bash command."}, 204
        return {"output": output.decode('utf-8')}, 200
    except subprocess.CalledProcessError as e:
        print("Bash command failed with code:", e)
        return {"error": "Failed to execute bash command."}, 500