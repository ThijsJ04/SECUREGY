from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/execute_bash', methods=['POST'])
def execute_bash():
    data = request.get_json()
    if 'command' not in data:
        return "Error: Missing command", 400

    cmd = data.pop('command')
    try:
        process = subprocess.Popen(cmd, shell=True)
        output, err = process.communicate()
        if err:
            return f"Error executing command '{cmd}': {err.decode('utf-8')}", 500
        return cmd + " is done\n" if output else cmd
    except Exception as e:
        return str(e), 500