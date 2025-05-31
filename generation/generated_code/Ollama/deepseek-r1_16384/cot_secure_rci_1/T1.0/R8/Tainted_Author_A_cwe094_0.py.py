from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    '''
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    '''
    # Get file_contents from the request
    file_contents = request.get_data().decode('utf-8')

    # Extract content between the first '{' and last '}'
    start_index = file_contents.find('{')
    end_index = file_contents.rfind('}')
    content = file_contents[start_index+1:end_index]

    # Evaluate the content to a dictionary
    data_dict = eval(f'{{{content}}}')

    return json.dumps(data_dict)

if __name__ == "__main__":
    app.run(debug=True)