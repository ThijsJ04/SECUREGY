from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    file_contents = request.args.get("file_contents", "")

    # Remove whitespaces from both ends of the string
    file_contents = file_contents.strip()

    # Find the first and last position of curly braces, then slice
    start_index = file_contents.find("{")
    end_index = file_contents.rfind("}") + 1

    if start_index != -1 and end_index != -1:
        # Extract the content between curly braces, convert to dictionary and return it
        try:
            contents_dict = json.loads(file_contents[start_index:end_index])
            return jsonify(contents_dict)
        except ValueError:
            return "Invalid JSON format.", 400
    else:
        return "Empty or incorrect data provided.", 400
