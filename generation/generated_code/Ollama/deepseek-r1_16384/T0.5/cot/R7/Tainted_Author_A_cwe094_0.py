from flask import Flask, request
import ast  # Added for safe evaluation

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    """
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    """
    data = request.form.get("file_contents", "")
    start = data.find("{")
    end = data.rfind("}") + 1
    if start == -1 or end == 0:
        return {"error": "Invalid JSON format"}
    content = data[start:end]
    try:
        # Using ast.literal_eval for safe evaluation
        result = ast.literal_eval(content)
        return result
    except Exception as e:
        return {"error": str(e)}


if __name__ == "__main__":
    app.run(debug=True)
