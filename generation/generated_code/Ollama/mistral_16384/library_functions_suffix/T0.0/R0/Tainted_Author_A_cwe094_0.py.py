from mimetypes import MimeTypes
  import json
  from flask import Flask, request

  app = Flask(__name__)

  @app.route('/eval')
  def contents_dict():
      file_type = MimeTypes().guess_extension(request.headers['Content-Type'])
      if file_type == 'application/json':
          return json.loads(request.data)
      else:
          data = request.data.decode('utf-8')
          start = data.find('{') + 1
          end = len(data) - data[-1:].rfind('}')
          content = data[start:end]
          return eval(content)