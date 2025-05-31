import subprocess
import os
from flask import Flask, request

app = Flask(__name__)

bash_commands = {
 'mkdir': lambda x: 'rm -rf {}'.format(x),
 'cd': None
}

@app.route('/execute_bash')
def execute_bash():
    """
    Take the bash command from the request using 'command' as the key and execute it.
    Return the command.
    """
    try:
        command = os.path.join(os.getcwd(), str(request.args['command']))
        if not os.path.exists('/tmp') or not os.access('/tmp', os.W_OK):
            raise Exception("/tmp does not exist")
        subprocess.check_call(command, shell=True)
    except KeyError:
        return "Missing command argument."
    except FileNotFoundError as e:
        return str(e)