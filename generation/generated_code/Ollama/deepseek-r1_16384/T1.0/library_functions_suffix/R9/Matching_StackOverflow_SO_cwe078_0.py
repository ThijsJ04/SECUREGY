import subprocess
import os
from flask import Flask, request
import shlex

app = Flask(__name__)


@app.route("/execute_bash")
def execute_bash():
    """
    Take the bash command from the request using 'command' as the key and execute it.
    Return the command output or an error message if something goes wrong.
    """
    cmd = request.args.get("command", None)
    if not cmd:
        return {"error": "No command provided"}, 400

    try:
        # Split the command safely
        args = shlex.split(cmd)
        result = subprocess.run(args, capture_output=True, text=True, check=False)

        if result.returncode == 0:
            return {"success": True, "output": result.stdout}
        else:
            return {
                "success": False,
                "error": f"Command failed with error: {result.stderr}",
            }, 400

    except Exception as e:
        return {"error": str(e)}, 500


if __name__ == "__main__":
    app.run(debug=True)
