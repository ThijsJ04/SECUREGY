# Import necessary modules
from flask import Flask, request

# Create the Flask application instance
app = Flask(__name__)

# Define a route for the /eval endpoint
@app.route('/eval', methods=['GET', 'POST'])
def eval_contents():
    # Get file contents from the request
    content = request.files.get('file_contents')

    if not content:
        return "No file uploaded"

    # Remove leading and trailing whitespace and newline characters
    content = ''.join(content).strip()

    # Evaluate the content as a Python expression using eval()
    result = eval(content)

    return result