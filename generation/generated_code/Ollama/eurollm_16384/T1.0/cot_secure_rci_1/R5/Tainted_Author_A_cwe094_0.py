from flask import Flask, request

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    content = request.get("file_contents")
    # Now we've got a string, and 'content' is the variable that contains this string.
    # Let's use it in the function.

    # To remove everything before the first { (or after the last }, do this:
    cleaned_content = content.split("}")[0].split("{")[-1]

    return {
        **{"cleaned_file": cleaned_content}
    }  # unpacks to the dictionary key-value pair we want
