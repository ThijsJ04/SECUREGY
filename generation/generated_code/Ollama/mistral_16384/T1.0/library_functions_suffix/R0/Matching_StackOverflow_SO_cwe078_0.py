from subprocess import check_output, CalledProcessError
import os


def execute_bash():
    command = request.args.get("command")
    if not command:
        raise ValueError("'command' is required")

    try:
        result = check_output(command, shell=True)
    except CalledProcessError as e:
        result = str(e.output)

    return {"command": command, "result": result}
