from flask import Flask, request

app = Flask(__name__)


def contents_dict(request):
    content = request.args.get("file_contents")
    parsed_content = ""

    # Check if there's any content provided
    if content:
        # Parse the content into a dictionary using eval
        parsed_content = eval(content)

        return str(parsed_content)
    else:
        return "No content provided"
