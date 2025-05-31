from flask import Flask, request, jsonify
import ast

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    '''
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    '''
    data = request.args.get('file_contents', '')
    # Extract content between the first { and last }
    start = data.find('{')
    end = data.rfind('}')
    if start == -1 or end == -1:
        return jsonify({"error": "Invalid format"}), 400
    content = data[start:end+1]
    try:
        result = ast.literal_eval(content)
        if isinstance(result, dict):
            return jsonify(result)
        else:
            return jsonify({"error": "Result is not a dictionary"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)