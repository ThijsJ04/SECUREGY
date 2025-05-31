import subprocess
import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/execute_bash')
def execute_bash():
    command = request.args.get('command')
    if not command:
        return "Command parameter is required", 400
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        output = result.stdout + result.stderr
        return output
    except Exception as e:
        return f"Error executing command: {str(e)}", 500

if __name__ == '__main__':
    app.run(debug=True)