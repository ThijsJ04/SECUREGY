from flask import Flask, request
import ast

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    try:
        # Get the data from the request using 'file_contents'.
        content = request.args.get("file_contents", default="")

        # Remove anything before the first '{' and after the last '}'.
        parsed_content = ast.parse(content).body[0].value

        # Evaluate the content as a dictionary.
        eval_dict = eval(str(parsed_content))

        return jsonify({"result": eval_dict})
    except Exception as e:
        print("An error occurred:", str(e))
        return {"error": "Invalid or unsupported data."}
