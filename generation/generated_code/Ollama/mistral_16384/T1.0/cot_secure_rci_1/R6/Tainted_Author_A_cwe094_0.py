from flask import Flask, request

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    """
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    """
    file_data = request.files["file_contents"].read().decode("utf-8")
    if "{" not in file_data or "}" not in file_data:
        return {"error": "Invalid JSON"}

    start_index = file_data.find("{")
    end_index = file_data.rfind("}") + 1
    json_data = file_data[start_index:end_index]
    return json.loads(json_data)
