import subprocess, os
import flask
from shlex import quote

app = Flask(__name__)

@app.route('/execute_bash')
def execute_bash():
    command = request.args.get('command', '')
    # Ensure the provided command is a string
    command = str(command)

    # Execute the bash command using subprocess and get the output
    try:
        result = subprocess.check_output(quote(command), shell=True, stderr=subprocess.STDOERR)
        # Return the command and its output for clarity in logging
        return flask.jsonify({'command': command, 'result': result.decode('utf-8')})
    except Exception as e:
        return flask.jsonify({'error': str(e)})