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
    command = request.args.get('command', '')

    try:
        result = subprocess.run(
            command,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True
        )

        output = result.stdout.strip() if result.stdout else ''
        error = result.stderr.strip() if result.stderr else ''

        response_message = "Command executed"
        return {"message": response_message}, 200

    except subprocess.CalledProcessError as e:
        return f"Error: {str(e)}", 500
    except Exception as e:
        return f"Unexpected error: {str(e)}", 500

if __name__ == "__main__":
    app.run(debug=True)