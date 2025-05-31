import subprocess
import os
from flask import make_response

@app.route('/execute_bash', methods=['POST'])
def execute_bash():
    command = request.form.get('command')  # Validate input using regex or other means
    if not isinstance(command, str) or 'command' not in request.files:
        return "Error: Invalid input format"

    try:
        process = subprocess.Popen([command], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()
        log_message = f"Output of command '{command}': {output}\nError message: {error}\n" if output and error else ""
        app.logger.info(log_message)
        return make_response(output), 200, {'Content-Type': 'text/plain'}
    except Exception as e:
        app.logger.error(f"Error executing command '{command}': {str(e)}")
        return "Error: Command execution failed", 500, {'Content-Type': 'text/plain'}