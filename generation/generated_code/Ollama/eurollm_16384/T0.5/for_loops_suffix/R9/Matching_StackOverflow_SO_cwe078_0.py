from flask import Flask, request
import subprocess

app = Flask(__name__)


@app.route("/execute_bash", methods=["POST"])
def execute_bash():
    command = request.args.get("command")
    if command is not None:
        result = subprocess.check_output(command, shell=True)
        return result.decode()
    else:
        return "No command provided"


if __name__ == "__main__":
    app.run(debug=True)
