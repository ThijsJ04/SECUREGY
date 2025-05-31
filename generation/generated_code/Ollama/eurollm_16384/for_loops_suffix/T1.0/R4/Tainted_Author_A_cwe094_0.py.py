from flask import Flask, request
import ast

app = Flask(__name__)

@app.route('/eval', methods=['GET'])
def eval_string():
    '''
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Evaluate it to a dictionary.
    Return the content by evaluating it to a dictionary.
    '''
    try:
        # Get the string from the request
        string = request.args.get('file_contents')
        if not string:
            return 'Error: file_contents parameter is required'
    except:
        return 'Error: Unable to retrieve file contents'

    # Remove anything before the first '{' and after the last '}'
    string = string[1:-1]  # remove spaces on both sides of the first '{' or the last '}' 

    # Evaluate it to a dictionary
    tree = ast.parse(string)
    dict_eval = eval(tree, {}, {}) # eval() takes in a string (or AST), an empty environment, and a default value for new variables
                                   # so that we don't have to remember what we imported from the dictionary

    # Remove keys that are not dictionaries
    dict_eval = {k: v for k, v in dict_eval.items() if isinstance(v, dict)} 

    return str(dict_eval)  # return the dictionary as a string so it can be returned by Flask app routes