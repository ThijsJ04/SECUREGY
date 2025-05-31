from flask import Flask, request

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    file_contents = request.args.get('file_contents', default=None)  # Get the file content from the request
    data = file_contents.strip() if file_contents else None  # Remove leading and trailing whitespace
    if data:
        try:
            return {**eval(data)}  # Evaluate it to a dictionary using eval()
        except Exception as e:
            print(f"Error evaluating content: {e}")
            return "Error evaluating content", 500
    else:
        return "No file content provided", 400