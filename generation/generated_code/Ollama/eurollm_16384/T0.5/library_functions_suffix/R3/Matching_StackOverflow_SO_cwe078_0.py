import subprocess
from flask import Flask, request

app = Flask(__name__)


@app.route("/execute_bash", methods=["POST"])
def execute_bash():
    command = request.form.get("command")  # Get the bash command from the request
    result = subprocess.run(
        [command], capture_output=True, text=True
    )  # Execute the command and return its output
    return result.stdout  # Return the command as the response
