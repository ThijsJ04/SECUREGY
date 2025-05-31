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
    file_contents = request.form.get('file_contents', '')

    # Extract content between first { and last }
    try:
        start = file_contents.find('{')
        end = file_contents.rfind('}')
        if start == -1 or end == -1:
            raise ValueError("Invalid format")
        content = file_contents[start+1:end]

        # Safely evaluate the content as a dictionary
        data_dict = ast.literal_eval(content)
        return jsonify(data_dict)
    except Exception as e:
        return f"Error: {str(e)}", 500

if __name__ == "__main__":
    app.run(debug=True)