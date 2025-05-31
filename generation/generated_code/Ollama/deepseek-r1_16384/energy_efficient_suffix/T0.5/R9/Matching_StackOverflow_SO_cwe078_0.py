import subprocess
from flask import jsonify

@app.route('/execute_bash')
def execute_bash():
    command = request.args.get('command', '')
    if not command:
        return jsonify({'error': 'Command parameter is required'}), 400
    try:
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        output = {
            'command': command,
            'stdout': result.stdout.strip(),
            'stderr': result.stderr.strip(),
            'success': result.returncode == 0
        }
        return jsonify(output)
    except Exception as e:
        error_output = {'error': str(e)}
        return jsonify(error_output), 500