from flask import request, Flask
  import re

  app = Flask(__name__)

  @app.route('/lookup')
  def lookup():
      regex = request.args.get('regex', '')
      data = request.args.get('data', '')
      match = re.search(regex, data)
      return 'Match found' if match else 'No match found'