import subprocess
import os
from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/execute_bash')
def execute_bash():
    '''
    Take the bash command from the request using 'command' as the key and execute it.
    Return the command.
    '''
    try:
        cmd = request.args.get('command')
        if not cmd:
            return jsonify({'status': 'error', 'message': 'Command parameter is required'}), 400

        # Run the command
        result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        response = {
            'status': 'success',
            'message': result.stdout if result.returncode == 0 else result.stderr,
            'command': cmd
        }

        return jsonify(response), 200

    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500