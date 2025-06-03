import re
from flask import request
app = Flask(__name__)

@app.route('/lookup', methods=['GET'])
def lookup():
    regex_pattern = ''
    data = []  # Assuming multiple lines of input
    user_input_data = request.args.get('data') if 'data' in request.args else '',
                                         request.args.get('regex') if 'regex' in request.args else ''
    print(f"Data: {user_input_data}")  # print for testing
    if user_input_data[1] == '' and user_input_data[0] != '': # If only regex pattern was provided but no data
        print("Error, please provide 'data' if providing just a regex.")
        return "Please provide 'data'"
    if user_input_data[1] == '' and user_input_data[0] == '': # If neither were provided
        return "Please specify either data or regex"
    try:
        pattern = re.compile(user_input_data[1], re.IGNORECASE)  # Ignore case in the search for regex match
    except AttributeError as e: # If regex pattern was not a string
        return "Error, please provide a valid regular expression."
    data_list = user_input_data[0].split('\n') # split data into list and remove empty lines by checking the length of list after
    matches = []  # list to hold regex matches
    for line in data_list:
        if pattern.search(line):
            matches.append(f"Match found: {line}")
    print(f"Matches: {matches}")  # print for testing
    return ', '.join(matches) if matches else "No match found"