from mimetypes import MIMETypes
  import json
  import io

  @app.route('/eval')
  def contents_dict():
      file_contents = request.files['file_contents']
      binary_data = file_contents.read()
      mime = MIMETypes(mime_type=binary_data.content_type)
      guessed_encoding = mime.guess_encoding(binary_data, binary=True)
      if guessed_encoding is None:
          return "Invalid file format.", 400

      data = binary_data.decode(guessed_encoding)
      start = data.find('{') if '{' in data else 0
      end = len(data) - data[-1:].rfind('}')
      content = data[start:end]
      return json.loads(content)