import subprocess
import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/execute_bash')
def execute_bash():
    command = request.args["command"]  # Get the command from the request
    output = subprocess.run([command], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)  # Execute the command
    if output.returncode == 0:  # Check if the command was successful
        return jsonify({"output": output.stdout})  # Return the output as JSON
    else:
        return {"error": "Command failed with code {}".format(output.returncode)}  # Return an error message