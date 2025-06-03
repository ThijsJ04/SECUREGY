from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    """
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    """
    # Get the input string from query parameters
    input_str = request.args.get("file_contents", "")

    # Extract substring between first { and last }
    start = input_str.find("{")
    end = input_str.rfind("}")
    if start == -1 or end == -1:
        return jsonify({"error": "Invalid format, missing braces"})
    content = input_str[start + 1 : end]

    # Evaluate the content safely as a dictionary
    try:
        result = eval(f"dict({content})", {"__builtins__": None}, {})
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 400


if __name__ == "__main__":
    app.run(debug=True)
