from flask import Flask, request
import json

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    file_contents = request.args.get("file_contents", None)

    if file_contents:
        # Remove anything before the first '{' and after the last '}'
        cleaned_json = file_contents[file_contents.find("{") :]
        cleaned_json = cleaned_json[: cleaned_json.rfind("}") + len("}")]

        try:
            # Evaluate the content to a dictionary
            return json.loads(cleaned_json)
        except ValueError as e:
            return str(e), 400  # Return an error message if the JSON cannot be loaded
