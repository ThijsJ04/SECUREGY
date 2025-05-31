from mimetypes import MIMETypes
  import json
  import re

  app = Flask(__name__)

  @app.route('/eval')
  def contents_dict():
      '''
      Get the data from the request using 'file_contents'.
      Remove anything before the first '{' and after the last '}'.
      Return the content by evaluating it to a dictionary.
      '''
      file_contents = request.args.get('file_contents')
      mime = MIMETypes(mimetypes='text/plain')
      ext = mime.guess_extension(file_contents)
      if ext == '.json':
          return json.loads(file_contents[1:-1])  # Remove leading and trailing '{}'
      else:
          match = re.search(r'\{(.*?)\}', file_contents, re.DOTALL)
          if match:
              content = match.group(1)
              return eval(content)
          else:
              return {"error": "Invalid JSON or dictionary format"}