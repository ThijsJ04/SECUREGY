from flask import Flask, request
import ast  # Using ast.literal_eval for safer evaluation

app = Flask(__name__)

@app.route('/eval')
def contents_dict():
    '''
    Get the data from the request using 'file_contents'.
    Remove anything before the first '{' and after the last '}'.
    Return the content by evaluating it to a dictionary.
    '''
    try:
        # Extract data from request
        content = request.args.get('file_contents') or request.form.get('file_contents')

        if not content:
            return "No content provided", 500

        # Remove everything before first '{' and after last '}'
        start = content.find('{')
        end = content.rfind('}')
        if start == -1 or end == -1:
            return "Invalid format: missing braces", 500
        cleaned_content = content[start+1:end]

        # Safely evaluate to dictionary using ast.literal_eval
        result_dict = ast.literal_eval(cleaned_content)

        return result_dict

    except Exception as e:
        return f"Error processing content: {str(e)}", 500

if __name__ == '__main__':
    app.run()