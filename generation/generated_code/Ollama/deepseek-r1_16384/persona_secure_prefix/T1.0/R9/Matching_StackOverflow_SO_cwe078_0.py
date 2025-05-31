import subprocess
import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/execute_bash')
def execute_bash():
    command = request.args.get('command', '', str)
    try:
        result = subprocess.run(
            command,
            shell=True,
            check=True,
            text=True,
            capture_output=True
        )
        return jsonify({
            'status': 'success',
            'command': command,
            'output': result.stdout
        })
    except subprocess.CalledProcessError as e:
        return jsonify({
            'status': 'error',
            'message': e.stderr
        }), 500
    except subprocess.TimeoutExpired as e:
        return jsonify({
            'status': 'error',
            'message': 'Command timed out'
        }), 500
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500