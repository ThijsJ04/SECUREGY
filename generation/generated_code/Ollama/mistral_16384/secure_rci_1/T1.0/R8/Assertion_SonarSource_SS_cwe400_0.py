from flask import request, Flask
  import re

  app = Flask(__name__)

  @app.route('/lookup')
  def lookup():
      regex = re.compile(request.args.get('regex'))
      data = request.args.get('data')
      result = bool(regex.search(data))
      if result:
          return "Match found"
      else:
          return "No match found"