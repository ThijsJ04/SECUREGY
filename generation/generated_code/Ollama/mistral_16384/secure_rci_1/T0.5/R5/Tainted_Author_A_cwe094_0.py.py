from mimetypes import MIMETypes
  import json
  import re

  app = Flask(__name__)

  @app.route('/eval')
  def contents_dict():
      data = request.headers.get('file_contents')
      if not data:
          return {"error": "No data provided"}, 400

      # Remove any characters before the first '{' and after the last '}'
      cleaned_data = re.sub(r'^{|}$', '', data)

      try:
          # Evaluate the string as a dictionary
          return json.loads(cleaned_data), 200
      except ValueError:
          return {"error": "Invalid JSON"}, 400