from flask import Flask, request

  app = Flask(__name__)

  @app.route('/eval')
  def contents_dict():
      data = request.args.get('file_contents', None)
      if data:
          data = data.strip('{}')  # remove leading and trailing curly braces
          try:
              return {k: v for k, v in ast.literal_eval(data).items()}
          except SyntaxError:
              return {}

  if __name__ == '__main__':
      app.run()