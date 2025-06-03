from flask import Flask, request

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    data = request.args.get(
        "file_contents", default="example"
    )  # Get file contents from the request URL
    # Remove anything before the first '{' and after the last '}'
    data = data[data.find("{") + 1 : data.rfind("}")]
    # Evaluate the content to a dictionary (Note: this will raise an exception if it can't evaluate)
    try:
        result = eval(data)
    except Exception as e:
        return "Error evaluating data: %s" % str(
            e
        )  # return error message in case of exception
    else:
        # return the result dictionary or a default value if the evaluation failed
        if (
            len(result) > 0 and type(result[0]) == dict
        ):  # if at least one element is a dict, assume this is the right content structure
            return str(
                [eval(sub_dict) for sub_dict in result]
            )  # flatten nested dictionaries using eval recursively
        else:
            return "Unknown data format."
