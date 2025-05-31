import subprocess
import os
from flask import Flask, request, jsonify

app = Flask(__name__)

def execute_bash_command(command):
    try:
        process = subprocess.Popen([command], shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        output, error = process.communicate()
        return output.decode('utf-8')
    except Exception as e:
        print(e)
        return {'error': 'Error executing command: %s' % str(e)}

@app.route('/execute_bash', methods=['POST'])
def execute_bash():
    command = request.json['command']
    result = execute_bash_command(command)
    return jsonify({'status': 'success', 'message': result}) if result else jsonify({'error': 'Command not found or unable to execute'})

if __name__ == '__main__':
    app.run()