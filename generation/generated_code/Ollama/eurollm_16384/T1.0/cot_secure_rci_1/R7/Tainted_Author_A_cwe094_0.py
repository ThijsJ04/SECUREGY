from flask import Flask, request

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    """
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    """
    string = request.args.get(
        "file_contents"
    )  # get 'file_contents' from the request using a GET parameter

    if not string:
        return "Missing data for file_contents"
    else:
        dict_data = eval(string)  # if the data is a dictionary, return it
        if type(dict_data).__name__ == "dict":
            return str(
                dict_data
            )  # if it is a dictionary, convert it to string before returning
    return "Invalid format for file_contents"
