import subprocess
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/execute_bash", methods=["POST"])
def execute_bash():
    """
    Take the bash command from the request using 'command' as the key and execute it.
    Return the command.
    """
    data = request.get_json()
    command = data.get("command")

    if not command:
        return jsonify({"error": "Command is required"}), 400

    try:
        subprocess.run(["bash", "-c", command], check=True, capture_output=True)
        return jsonify({"message": "Command executed successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
