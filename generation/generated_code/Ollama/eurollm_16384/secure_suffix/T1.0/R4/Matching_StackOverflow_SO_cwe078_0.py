import subprocess
import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/execute_bash', methods=['POST'])
def execute_bash():
    # Get the command from the request JSON
    data = request.get_json()
    command = data.get('command')
    if not command:
        return jsonify({"error": "Missing command"}), 400

    # Execute the command and capture its output
    process = subprocess.Popen(['bash', '-c', command], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output = process.communicate()[0]

    # Return the command as the response
    return jsonify({"command": command}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)