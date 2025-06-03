from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/eval", methods=["POST"])
def contents_dict():
    """
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    """
    try:
        # Get file contents from request
        post_data = request.get_json()["file_contents"]
        # Remove any leading or trailing whitespace and any non-valid characters before '{' and after '}'
        cleaned_data = ""
        for char in post_data:
            if char == "{" or char == "}":
                break
            cleaned_data += char if ord(char) < 128 else ""

        # Evaluate the cleaned data to a dictionary and return it as JSON response
        dict_response = eval(cleaned_data)
        return (
            jsonify({"result": str(dict_response)}),
            200,
            {"ContentType": "application/json"},
        )
    except Exception as e:
        return str(e), 500, {"ContentType": "text/plain"}
