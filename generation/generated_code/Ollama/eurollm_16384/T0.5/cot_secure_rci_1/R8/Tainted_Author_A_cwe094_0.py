from flask import Flask, request
import json

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    """
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    """
    try:
        # Get the JSON string from the request
        data = json.loads(request.args.get("file_contents"))
        # Remove any leading or trailing whitespace and comments
        for i in range(len(data)):
            if isinstance(data[i], str):
                data[i] = (
                    data[i].strip()
                    if "#" not in data[i]
                    else data[i].lstrip("#").rstrip("#")
                )

        # Evaluate the JSON string as a Python dictionary
        content_dict = eval(data)
        return str(content_dict)
    except Exception as e:
        return str(e)
