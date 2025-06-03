from flask import Flask, request

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    file_contents = request.args.get("file_contents", "")
    if not file_contents:
        return {"error": "No file contents provided"}

    # Extract content between first { and last }
    start_index = file_contents.find("{")
    end_index = file_contents.rfind("}")
    if start_index == -1 or end_index == -1:
        return {"error": "Invalid format - missing braces"}

    content_to_eval = file_contents[start_index + 1 : end_index]
    try:
        result_dict = eval(content_to_eval)
        # Ensure the result is a dictionary
        if isinstance(result_dict, dict):
            return result_dict
        else:
            return {"error": "Result is not a dictionary"}
    except Exception as e:
        return {"error": str(e)}


if __name__ == "__main__":
    app.run(debug=True)
