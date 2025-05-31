import subprocess
import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/execute_bash', methods=['POST'])
def execute_bash():
    command = request.args.get('command')
    if not command:
        return 'Command is required', 400

    # Execute the bash command using subprocess.run()
    result = subprocess.run(['bash', '-c', command], check=True)
    return result.stdout, 200

if __name__ == '__main__':
    app.run(debug=True)