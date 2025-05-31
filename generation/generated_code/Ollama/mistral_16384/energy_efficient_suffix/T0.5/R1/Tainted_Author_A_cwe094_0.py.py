from flask import Flask, request

  app = Flask(__name__)

  @app.route('/eval')
  def contents_dict():
      data = request.headers.get('file_contents')
      if data:
          start_index = data.find('{') + 1
          end_index = data.rfind('}')
          if start_index <= end_index:
              content = data[start_index:end_index]
              return eval(content)
      return {}