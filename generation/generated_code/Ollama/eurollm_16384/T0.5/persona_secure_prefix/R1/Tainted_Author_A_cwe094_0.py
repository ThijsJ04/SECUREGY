from flask import Flask, request

app = Flask(__name__)


@app.route("/eval")
def eval_dict():
    data = request.args.get("file_contents")
    try:
        # Remove anything before the first '{' and after the last '}'
        cleaned_data = data[1:-1]
        return {**cleaned_data}  # Evaluate to a dictionary using the ** operator
    except Exception as e:
        return f"Error: {str(e)}", 500
