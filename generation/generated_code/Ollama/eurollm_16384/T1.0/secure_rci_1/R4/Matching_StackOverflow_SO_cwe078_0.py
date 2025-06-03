# Import required modules
import subprocess  # Use subprocess instead of popen() from 2.x versions for more control
import os
from flask import Flask, request

# Create an instance of Flask application
app = Flask(__name__)


# Define a route to execute bash commands
@app.route("/execute_bash", methods=["POST"])  # Add GET and headers
def execute_bash():
    """
    Take the bash command from the request using 'command' as the key and execute it.
    Return the command.
    """

    # Get the command from the request
    command = request.form["command"]
    # Remove leading and trailing whitespace from the command
    command = command.strip()

    # Execute the command and return it
    result = subprocess.check_output(
        command, shell=True
    )  # Use subprocess instead of popen() for more control
    return result.decode("utf-8").strip()
