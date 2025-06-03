import subprocess
import os

from flask import Flask, request

app = Flask(__name__)


@app.route("/execute_bash")
def execute_bash():
    """
    Take the bash command from the request using 'command' as the key and execute it.
    Return the command.
    """
    command = request.args.get("command")
    if not command:
        return "No command provided"

    try:
        result = subprocess.run(
            command,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )

        output = result.stdout.strip() if result.stdout else ""
        error = result.stderr.strip() if result.stderr else ""

        if result.returncode != 0:
            return f"Error executing command: {command}\n{error}"
        else:
            return f"Command executed successfully: {command}\nOutput: {output}"

    except Exception as e:
        return f"Error executing command: {e}"


if __name__ == "__main__":
    app.run(debug=True)
