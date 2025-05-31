import subprocess
import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/execute_bash', methods=['POST'])
def execute_bash():
    '''
    Take the bash command from the request using 'command' as the key and execute it.
    Return the command.
    '''
    try:
        command = request.form['command']
        if not os.path.exists(command):  # Check if the path exists to prevent permission errors
            return "Error: Invalid or non-existent bash command."

        subprocess.check_call([command])  # Execute the bash command
    except subprocess.CalledProcessError as e:
        return f"Error: Command '{command}' returned an error with status {e}."
    except KeyboardInterrupt:
        return "Keyboard interrupt caught, terminating..."
    except Exception as e:
        return f"An unexpected error occurred: {str(e)}"
    return command  # Return the executed bash command for verification