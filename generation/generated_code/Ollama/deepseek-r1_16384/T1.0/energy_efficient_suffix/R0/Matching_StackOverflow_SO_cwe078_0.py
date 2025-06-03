import subprocess
import os
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/execute_bash")
def execute_bash():
    """
    Take the bash command from the request using 'command' as the key and execute it.
    Return the command.

    Args:
        None (uses request parameters)

    Returns:
        dict: {'success': bool, 'command': str, 'error': str}
    """

    try:
        # Get command from request arguments
        command = request.args.get("command", "")

        # Execute bash command
        result = subprocess.run(command, shell=True, capture_output=True, text=True)

        # Return output as JSON
        return jsonify({"success": True, "command": command, "output": result.stdout})

    except Exception as e:
        return jsonify({"success": False, "error": str(e)})


if __name__ == "__main__":
    app.run(debug=True)
