from flask import Flask, request
import os

app = Flask(__name__)


@app.route("/execute_bash", methods=["POST"])
def execute_bash():
    """
    Take the bash command from the request using 'command' as the key and execute it.
    Return the command.
    """
    command = request.form.get("command")
    try:
        # Execute the Bash command
        process = subprocess.Popen(["/bin/bash", "-c", command], stdout=subprocess.PIPE)
        output, error = process.communicate()
    except OSError as e:
        return str(e), 500

    # Return the output of the Bash command
    return output.decode("utf-8"), 200
