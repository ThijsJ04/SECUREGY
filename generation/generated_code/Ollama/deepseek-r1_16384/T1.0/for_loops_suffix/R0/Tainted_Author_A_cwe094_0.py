from flask import Flask, request
import ast

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    file_contents = request.args.get("file_contents", "")
    content = file_contents.split("{")[1].split("}")[0]
    return ast.literal_eval(f"{{{content}}}")


if __name__ == "__main__":
    app.run(debug=True)
