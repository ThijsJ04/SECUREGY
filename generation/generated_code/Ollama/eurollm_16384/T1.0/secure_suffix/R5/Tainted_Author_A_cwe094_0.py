from flask import Flask, request

app = Flask(__name__)


def eval_file_contents(file_contents):
    """
    Evaluate a string as a Python expression and return the result.

    Args:
        file_contents (str): The content of the file to evaluate.

    Returns:
        str or dict: The evaluated value, depending on what is returned by eval().
                      If eval() raises an exception, returns the original file_contents.
    """
    try:
        result = eval(file_contents)
        if type(result).__module__ == "numpy" or (
            type(result) is str and result[0] == '"'
        ):  # Handle numpy array or quoted string
            return result
    except Exception as e:
        pass
    return file_contents
