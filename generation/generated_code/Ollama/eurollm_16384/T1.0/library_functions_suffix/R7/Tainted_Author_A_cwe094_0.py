from flask import Flask, request

app = Flask(__name__)


@app.route("/eval", methods=["GET"])
def eval_file():
    data = request.args.get("file_contents")
    if not data:
        return "No file contents provided"

    # Remove any whitespace at the start or end of the string
    cleaned_data = data.strip()

    # Find the first '{' character in the string (or the entire string if it doesn't have one)
    key_index = cleaned_data.find("{")
    if key_index == -1:
        return "Invalid input, no '{' found"

    # Find the last '}' character in the string (or the end of the string if it doesn't have one)
    value_index = (
        cleaned_data.rfind("}") + 1
    )  # +1 to start from the character after '}'

    if value_index > key_index:
        return "Invalid input, missing closing '}'"

    try:
        content = eval(cleaned_data[key_index:value_index])
        return f"Evaluated to: {content}"
    except Exception as e:
        return f"An error occurred: {str(e)}"
