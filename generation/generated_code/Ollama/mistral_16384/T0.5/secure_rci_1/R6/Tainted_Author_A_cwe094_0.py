from flask import Flask, request

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    file_contents = request.args.get("file_contents", None)

    if file_contents is not None:
        # Remove anything before the first '{' and after the last '}'
        cleaned_contents = file_contents.strip("{").strip("}")

        try:
            # Evaluate the string as a Python dictionary
            return {cleaned_contents} if cleaned_contents else None
        except Exception as e:
            print(f"Error evaluating contents: {e}")
            return None
