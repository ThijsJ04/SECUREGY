from mimetypes import MimeTypes
  import json, io
  import ast

  app = Flask(__name__)

  @app.route('/eval')
  def contents_dict():
      file_contents = request.files['file_contents']
      raw_data = file_contents.read().decode('utf-8')
      start_index = raw_data.find('{') + 1
      end_index = len(raw_data) - raw_data[-1:]*len(raw_data) - raw_data[:raw_data.rfind('}')]
      content = raw_data[start_index:end_index]
      return json.loads(content)