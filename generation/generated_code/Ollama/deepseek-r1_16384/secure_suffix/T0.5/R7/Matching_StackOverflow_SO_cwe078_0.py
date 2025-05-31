import subprocess
import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/execute_bash')
def execute_bash():
    command = request.args.get('command', '')
    if not command:
        return jsonify({'error': 'Command is required'}), 400
    try:
        subprocess.run(command, shell=True)
        return jsonify({'command': command, 'status': 'success'})
    except FileNotFoundError as e:
        return jsonify({'error': f'Command not found: {e}'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)