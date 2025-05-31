from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/eval', methods=['GET'])
def eval_content():
    data = request.args.get("file_contents")
    if not data:
        return "Missing 'file_contents' parameter", 400

    try:
        content = json.loads(data) if isinstance(data, str) else eval(data)
        return {"content": content}
    except Exception as e:
        return {"error": str(e)}, 500