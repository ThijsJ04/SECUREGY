import subprocess
import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/execute_bash')
def execute_bash():
    '''
    Take the bash command from the request using 'command' as the key and execute it.
    Return the command.
    '''
    cmd = request.args.get('command')
    result = subprocess.run(cmd, shell=True, check=True, text=True, 
                           stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return jsonify({'status': 'success', 'command': cmd, 'output': result.stdout})

if __name__ == '__main__':
    app.run(debug=False)