import subprocess
import os
from flask import Flask, request

app = Flask(__name__)

def execute_bash(command):
    """
    Execute a bash command and return the output.

    Args:
        command (str): The bash command to be executed.

    Returns:
        str: The output of the executed command.
    """
    try:
        # Execute the bash command using subprocess.run
        output = subprocess.check_output(command, shell=True)
        return output.decode('utf-8')  # return the decoded output as a string
    except subprocess.CalledProcessError:
        # Handle cases where the command execution fails
        print("Command failed with code {}".format(subprocess.call()))