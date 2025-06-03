from flask import Flask, request

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    """
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    """
    file_contents = request.args.get("file_contents", "")

    # Extract the substring between the first '{' and last '}'
    if "{" in file_contents:
        start_index = file_contents.find("{")
        file_contents = file_contents[start_index:]
    else:
        return "No opening brace found", 400

    if "}" in file_contents:
        end_index = file_contents.rfind("}") + 1
        content = file_contents[:end_index]
    else:
        return "No closing brace found", 400

    # Evaluate the cleaned content as a dictionary
    try:
        data = eval(f"{{ {content} }}" if content else "{}")
        return data, 200
    except:
        return f"Invalid content: {content}", 400


if __name__ == "__main__":
    app.run(debug=True)
