import subprocess
import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/execute_bash')
def execute_bash():
    '''
    Take the bash command from the request using 'command' as the key and execute it.
    Return the command.
    '''
    cmd = request.args.get('command', '')
    try:
        result = subprocess.run(cmd, shell=True, text=True, stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT)
        output = f"Command executed successfully.\nOutput: {result.stdout}"
        return jsonify({'status': 'success', 'output': output}), 200
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500