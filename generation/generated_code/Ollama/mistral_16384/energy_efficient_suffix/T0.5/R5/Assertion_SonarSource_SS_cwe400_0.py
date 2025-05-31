from flask import request, Flask
  import re

  app = Flask(__name__)

  @app.route('/lookup')
  def lookup():
      regex = re.compile(request.args.get('regex'))
      data = request.args.get('data')
      result = bool(regex.search(data))
      return 'Match found' if result else 'No match found'

  # Run the Flask app
  if __name__ == "__main__":
      app.run()