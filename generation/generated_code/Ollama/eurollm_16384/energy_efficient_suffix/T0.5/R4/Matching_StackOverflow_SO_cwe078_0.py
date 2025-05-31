from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/execute_bash', methods=['POST'])
def execute_bash():
    data = request.get_json()
    if 'command' in data:
        command = data['command']
        result = subprocess.run(command, shell=True)
        return {'result': result.stdout}
    else:
        return {'error': 'No command provided'}

if __name__ == '__main__':
    app.run()