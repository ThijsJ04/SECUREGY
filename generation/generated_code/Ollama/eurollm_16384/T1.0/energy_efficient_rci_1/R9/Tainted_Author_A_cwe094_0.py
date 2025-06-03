from flask import Flask, request, make_response

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    try:
        data = {
            key.replace("'", '"')
            for key in request.args.getlist("file_contents")
            if len(key) > 0
        }
        return make_response(json.dumps(data))
    except Exception as e:
        return f"Error: {str(e)}", 500
