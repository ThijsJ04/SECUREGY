import subprocess
import os
from flask import request
from flask_cors import CORS
from werkzeug.exceptions import HTTPException

app = Flask(__name__)
CORS(app)


@app.route("/execute_bash", methods=["POST"])
def execute_bash():
    try:
        # Extract the command from the request data
        command = request.form.get("command")
    except KeyError as e:
        return "Invalid input. Make sure to pass a 'command' key in your POST request."

    # Execute the bash command
    process = subprocess.Popen(command, stdout=subprocess.PIPE)

    output, error = process.communicate()
    if not error:  # Check if the command was executed successfully
        return f"Command executed successfully:\n{output}"
    else:
        raise HTTPException(
            status_code=500, detail="Failed to execute command"
        ) from error
