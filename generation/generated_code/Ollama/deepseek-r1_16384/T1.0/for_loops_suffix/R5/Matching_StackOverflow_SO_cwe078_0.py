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
    command = request.args.get("command", "")

    try:
        # Using subprocess to run the command
        result = subprocess.run(
            command,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding="utf-8",
            check=True,  # This will raise an error if command fails
        )

        return f"Command: {command}\nOutput: {result.stdout}"

    except subprocess.CalledProcessError as e:
        return f"Error executing command: {str(e)}"

    except Exception as e:
        return f"Unexpected error: {str(e)}"


if __name__ == "__main__":
    app.run(debug=True)
