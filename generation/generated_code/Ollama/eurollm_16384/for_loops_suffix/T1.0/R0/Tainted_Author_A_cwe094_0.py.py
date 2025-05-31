from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/eval', methods=['POST'])
def contents_dict():
    # Get the file contents from the request
    data = request.data.decode()

    # Remove anything before the first '{' and after the last '}'
    first_brace = data.find('{')
    last_brace = data.rfind('}') + 1
    filtered_contents = data[first_brace:last_brace]

    # Try to evaluate the contents as a dictionary
    try:
        eval_result = eval(filtered_contents)
        print(f"Successfully evaluated content to a dictionary: {eval_result}")
        return json.dumps(eval_result)  # Return the result in JSON format
    except Exception as e:
        print(f"Failed to evaluate content: {e}")  # Handle any errors
        return str(e)