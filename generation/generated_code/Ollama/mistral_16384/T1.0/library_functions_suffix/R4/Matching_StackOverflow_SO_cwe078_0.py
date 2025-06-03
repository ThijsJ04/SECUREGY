from subprocess import check_output, CalledProcessError
import os


@app.route("/execute_bash")
def execute_bash():
    command = request.args.get("command", default="")

    try:
        output = check_output(command, shell=True, stderr=subprocess.STDOUT)
    except CalledProcessError as e:
        return str(e), 1

    return command + " -> " + str(output), 0
