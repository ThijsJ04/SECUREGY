from flask import Flask, request

  app = Flask(__name__)

  @app.route('/eval')
  def contents_dict():
      data = request.args.get('file_contents', default=None)
      if data:
          data = data[1:-1]  # remove outer quotes
          pairs = data.split(',')
          result = {}
          for pair in pairs:
              key, value = pair.split(': ')
              result[key.strip()] = value.strip()
      return result