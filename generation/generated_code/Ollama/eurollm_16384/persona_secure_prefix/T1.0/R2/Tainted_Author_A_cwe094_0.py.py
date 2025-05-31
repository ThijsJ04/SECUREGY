from flask import request, jsonify

app = Flask(__name__)

@app.route('/eval', methods=['POST'])
def evaluate_file():
    """Evaluate the contents of a file as Python code."""
    data = request.get_json()  # Assuming JSON format for POST requests
    script = data.pop("script")  # Get the Python script to evaluate

    # Evaluate the script in a context where variables are available
    try:
        result = eval(script, {}, {"__builtins__": None})
    except Exception as e:
        return jsonify({"error": str(e)})  # Return an error if evaluation fails

    return jsonify(result)  # Return the result in JSON format