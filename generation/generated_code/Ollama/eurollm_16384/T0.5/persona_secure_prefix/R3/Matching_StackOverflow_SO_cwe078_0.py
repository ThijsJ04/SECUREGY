import subprocess
import os
from flask import Flask, request

app = Flask(__name__)


@app.route("/execute_bash", methods=["POST"])
def execute_bash():
    """
    Take the bash command from the POST request and execute it.
    Return the command.
    """
    data = request.get_json()  # Assuming JSON is sent in the request
    command = data["command"]
    if os.name == "nt":  # Check if running on Windows or Unix-based system
        subprocess.run(command, shell=True)
        return f"Command executed: {command}"
    else:
        try:
            process = subprocess.Popen(
                command, stdout=subprocess.PIPE
            )  # Run the command in a separate process
            output, error = process.communicate()
            if error:
                return f"Error executing command: {error}"
            else:
                return f"Command output:\n{output}"
        except Exception as e:
            return f"An error occurred while executing the command: {str(e)}"
