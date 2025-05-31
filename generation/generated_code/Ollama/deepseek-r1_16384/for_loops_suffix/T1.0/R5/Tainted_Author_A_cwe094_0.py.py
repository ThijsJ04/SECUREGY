from flask import Flask, request

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    '''
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    '''
    # Retrieve the file_contents parameter from the request
    file_data = request.form.get('file_contents', '')

    # Extract the substring between the first '{' and last '}'
    start = file_data.find('{')
    end = file_data.rfind('}')
    if start == -1 or end == -1:
        return {}
    cleaned_data = file_data[start:end+1]

    try:
        # Evaluate the cleaned string as a dictionary
        result = eval(cleaned_data)
        return result
    except Exception:
        # Return empty dict if evaluation fails
        return {}

if __name__ == '__main__':
    app.run(debug=True)