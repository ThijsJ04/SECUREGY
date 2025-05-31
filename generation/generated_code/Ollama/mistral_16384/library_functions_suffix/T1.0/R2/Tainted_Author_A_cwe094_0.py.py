from mimetypes import MIMETypes
  import json, io

  @app.route('/eval')
  def contents_dict():
      data = request.files['file_contents'].read()
      buffer = io.StringIO(data.decode())
      mime = MIMETypes().guess_type(data)[0]
      if mime != 'application/json':
          return "Error: Content is not a valid JSON.", 400

      result = json.load(buffer)
      return jsonify(result)