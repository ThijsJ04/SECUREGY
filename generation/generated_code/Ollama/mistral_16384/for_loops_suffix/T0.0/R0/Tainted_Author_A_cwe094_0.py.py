from mimetypes import MIMETypes
  import json
  import re

  app = Flask(__name__)

  @app.route('/eval')
  def contents_dict():
      file_contents = request.files['file_contents']
      content_type = MIMETypes().guess(file_contents.filename)
      if content_type == 'application/json':
          data = json.loads(file_contents.read().decode())
          return jsonify(data)
      else:
          # Remove anything before the first '{' and after the last '}'
          data = re.search(r'{\s*(.*?)\s*}', file_contents.read(), re.DOTALL).group(1)
          try:
              return jsonify(json.loads(data))
          except ValueError as e:
              return jsonify({"error": str(e)}), 400