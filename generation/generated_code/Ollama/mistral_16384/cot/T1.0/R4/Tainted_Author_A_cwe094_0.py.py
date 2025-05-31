from flask import Flask, request

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    file_contents = request.args.get('file_contents', None)

    if file_contents:
        # Remove whitespaces before and after the string
        cleaned_str = file_contents.strip()

        # Find the first '{' and last '}' indices in the cleaned string, then slice the content as a dictionary
        start_index = cleaned_str.find('{')
        end_index = cleaned_str.rfind('}') + 1

        if start_index != -1 and end_index != -1:
            json_content = cleaned_str[start_index:end_index]

            # Evaluate the JSON content as a dictionary
            return eval(json_content)

    return {}