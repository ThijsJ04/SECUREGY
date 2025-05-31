from mimetypes import MimeTypes
  import json, ast

  app = Flask(__name__)

  @app.route('/eval')
  def contents_dict():
      file_contents = request.form['file_contents']
      # Remove whitespaces and newlines
      cleaned_content = ''.join(filter(str.isalnum, file_contents))
      # Find the indexes of the first '{' and last '}'
      start_index = cleaned_content.find('{')
      end_index = cleaned_content.rfind('}')
      # Slice the content to get only the relevant part
      relevant_content = cleaned_content[start_index:end_index+1]
      # Convert the string to a dictionary using ast.literal_eval()
      return json.dumps(ast.literal_eval(relevant_content))