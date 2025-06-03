import subprocess, os
import flask

app = flask.Flask(__name__)


@app.route("/execute_bash")
def execute_bash():
    command = request.args.get("command")
    output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOME)
    return flask.jsonify({"command": command, "output": output.decode()})
