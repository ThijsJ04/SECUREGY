from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    '''
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    '''
    # Get the content from the request
    content = request.args.get('file_contents') or request.form.get('file_contents')

    # Extract the part between the first '{' and last '}'
    if not content:
        return jsonify({})

    start = content.find('{')
    end = content.rfind('}')

    if start == -1 or end == -1:
        return jsonify(content)  # Return as is if no braces found

    extracted = content[start:end+1]

    # Evaluate the extracted string to a dictionary
    try:
        result = eval(extracted)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)})