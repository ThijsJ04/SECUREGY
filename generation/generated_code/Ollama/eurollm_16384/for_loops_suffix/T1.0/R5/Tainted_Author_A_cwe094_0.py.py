from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/eval', methods=['POST'])
def contents_dict():
    file_name = request.form.get('file_contents')
    try:
        with open(file_name, 'r') as f:
            content = f.read()
        parsed_content = content.split('}', 1)[0]  # Split the content before the first '{' and take only the first part (if it exists)
        dict_result = json.loads(parsed_content) if parsed_content else None
        return str(dict_result) if dict_result else "None"
    except Exception as e:
        return f"Error: {str(e)}", 500

if __name__ == '__main__':
    app.run()