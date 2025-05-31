from flask import Flask, request

  app = Flask(__name__)

  @app.route('/eval')
  def contents_dict():
      data = request.headers.get('file_contents')
      if data:
          data = data[data.find('{'):]  # remove anything before the first '{'
          data = data[:data.rfind('}') + 1]  # remove anything after the last '}'
          return eval(data)  # evaluate it to a dictionary