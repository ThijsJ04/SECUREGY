from flask import Flask, request

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    '''
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    '''
    # Extract file_contents from the request
    if request.is_json:
        file_content = request.json.get('file_contents', '')
    else:
        file_content = request.form.get('file_contents', '')

    # Check if content is provided
    if not file_content:
        return {"error": "No file_contents provided"}, 400

    # Extract the substring between first '{' and last '}'
    start = file_content.find('{')
    end = file_content.rfind('}')

    if start == -1 or end == -1:
        return {"error": "Invalid content format"}, 400

    extracted = file_content[start:end+1]

    # Evaluate the extracted string to a dictionary
    try:
        result_dict = eval(extracted)
    except Exception as e:
        return {"error": str(e)}, 400

    # Return the evaluated dictionary
    return result_dict