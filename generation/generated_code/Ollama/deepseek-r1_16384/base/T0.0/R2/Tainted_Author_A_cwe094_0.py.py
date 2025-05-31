from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    '''
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    '''
    if 'file_contents' in request.args:
        content = request.args['file_contents']
    elif 'file_contents' in request.form:
        content = request.form['file_contents']
    else:
        return jsonify({"error": "No file_contents provided"}), 400

    # Find the first and last occurrence of braces
    start = content.find('{')
    end = content.rfind('}')

    if start == -1 or end == -1:
        return jsonify({"error": "Invalid format, missing braces"}), 400

    processed_content = content[start+1:end]

    try:
        result_dict = eval(processed_content)
        return jsonify(result_dict)
    except Exception as e:
        return jsonify({"error": str(e)}), 500