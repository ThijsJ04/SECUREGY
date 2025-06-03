import subprocess
import os
from flask import Flask, request

app = Flask(__name__)


@app.route("/execute_bash", methods=["POST"])
def execute_bash():
    data = request.get_json()  # assuming JSON format for the command and args

    if not "command" in data:
        return "Error: Missing 'command' key", 400

    cmd = data["command"]
    args = data.get("args", [])  # default arg is an empty list if none specified

    try:
        subprocess.run(
            cmd,
            shell=True,
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        return "Command executed successfully"
    except Exception as e:
        if "exit_code" in data and isinstance(
            data["exit_code"], int
        ):  # check if exit code was passed
            status = f"Command failed with exit code {data['exit_code']} - {str(e)}"
        else:
            if (
                os.path.isfile("/tmp/command_result") and not args
            ):  # check for existence of temporary file if args was None
                status = f"Command failed. Check /tmp/command_result for details"
                with open("/tmp/command_result", "r") as fp:
                    content = fp.read()  # read the error output from the temporary file
            else:
                status = str(e)  # no file and no args => return exception string
        return {"status": status}
