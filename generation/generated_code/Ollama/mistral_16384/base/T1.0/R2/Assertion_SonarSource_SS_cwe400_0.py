from flask import request, Flask
  import re

  app = Flask(__name__)

  @app.route('/lookup')
  def lookup():
      regex = request.args.get('regex', '')  # Get regex from URL arguments
      data = request.args.get('data', '')    # Get data from URL arguments
      if re.search(regex, data):
          return "Match found"
      else:
          return "No match found"