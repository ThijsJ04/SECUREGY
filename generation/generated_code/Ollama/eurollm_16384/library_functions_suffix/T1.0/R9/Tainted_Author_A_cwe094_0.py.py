from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/eval', methods=['POST'])
def eval_expression():
    '''
    Evaluate an expression as a JSON string and return the result.
    '''
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400

    # Remove anything before the first '{' and after the last '}'
    exp = data['expression'].strip('{}')

    try:
        content = eval(exp)
        return jsonify({'content': content})
    except Exception as e:
        return jsonify({"error": str(e)}), 500