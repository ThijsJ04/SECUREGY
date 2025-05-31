from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    file_contents = request.args.get('file_contents', None)

    if file_contents:
        # Remove whitespaces and newlines
        cleaned_contents = file_contents.replace(" ", "").replace("\n", "")

        # Find the index of the first '{' and last '}'
        start_index = cleaned_contents.find('{')
        end_index = cleaned_contents.rfind('}')

        if start_index != -1 and end_index != -1:
            # Slice the string to get only the dictionary content
            dict_content = cleaned_contents[start_index:end_index+1]

            try:
                # Evaluate the dictionary string to a Python dictionary
                return json.loads(dict_content)
            except ValueError as e:
                return str(e), 400
    else:
        return 'Missing file_contents parameter.', 400