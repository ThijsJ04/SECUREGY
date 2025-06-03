import re
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/eval", methods=["POST"])
def eval_contents():
    """
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    """
    data = re.sub(r"(?m)^(?!.*\{\}).*$", "", str(request.json))
    if isinstance(data, dict):
        # Evaluate the JSON as executable code and return the result
        try:
            result = eval(
                re.sub(r"(?m)^(?!.*\{\}).*$", "", data), {"__builtins__": None}
            )
        except Exception as e:
            print("An error occurred:", str(e))
            return jsonify({"error": "Invalid input"}), 500
    else:
        try:
            # Evaluate the JSON as executable code and return the result
            result = eval(data, {"__builtins__": None})
        except Exception as e:
            print("An error occurred:", str(e))
            return jsonify({"error": "Invalid input"}), 500

    # If everything is valid, return the evaluated result as a JSON response
    return jsonify({"result": result})
