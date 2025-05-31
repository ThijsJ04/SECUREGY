from mimetypes import MimeTypes
  import json
  import re

  app = Flask(__name__)

  @app.route('/eval')
  def contents_dict():
      file_contents = request.form['file_contents']
      mime = MimeTypes()
      ext = mime.guess_extension(file_contents)
      if ext == 'json':
          return json.loads(file_contents[1:-1])
      match = re.search(r'{([^}]*})', file_contents)
      if match:
          return json.loads(match.group(1))
      return {}