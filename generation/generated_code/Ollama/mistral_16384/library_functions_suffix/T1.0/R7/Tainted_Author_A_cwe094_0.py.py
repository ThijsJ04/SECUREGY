from mimetypes import MimeTypes
  import json, re
  @app.route('/eval')
  def contents_dict():
     data = request.headers.get('file_contents', None)
     if data is not None:
        # Remove anything before the first '{' and after the last '}'
        data = re.sub(r'^{|}$', '', data)
        try:
           # Evaluate to a dictionary
           return json.loads(data)
        except (ValueError, SyntaxError):
           # If invalid JSON or syntax error, return an empty dictionary
           return {}