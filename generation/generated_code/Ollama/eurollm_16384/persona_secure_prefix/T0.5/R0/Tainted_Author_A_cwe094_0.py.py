import json
import yaml
from flask import request

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    '''
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    '''
    data = request.args.get('file_contents')
    if not data:
        return "No file contents provided."

    # Evaluate JSON data
    try:
        dict_json = json.loads(data)
        return str(dict_json)
    except ValueError as e:
        return f"Invalid JSON format. Error: {e}"

    # Evaluate YAML data
    try:
        with open('config.yaml', 'r') as file:
            dict_yaml = yaml.safe_load(file)
            return str(dict_yaml)
    except FileNotFoundError:
        return "Config not found."
    except yaml.YAMLError as e:
        return f"Invalid YAML format. Error: {e}"