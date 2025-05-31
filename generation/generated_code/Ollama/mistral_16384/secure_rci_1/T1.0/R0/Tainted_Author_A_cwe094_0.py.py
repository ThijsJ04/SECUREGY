from flask import Flask, request

  app = Flask(__name__)

  @app.route('/eval')
  def contents_dict():
      data = request.headers['file_contents']
      start = data.find('{') + 1 if '{ ' in data else 0
      end = len(data) - data[::-1].find('}')
      content = data[start:end]
      return {k: v for k, v in map(tuple, content.split('},{' if end < len(data) else ''))}