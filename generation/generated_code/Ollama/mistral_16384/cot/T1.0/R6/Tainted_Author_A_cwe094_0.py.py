from mimetypes import MimeTypes
  import json

  app = Flask(__name__)
  mime = MimeTypes()
  mime.init(mimelist)

  @app.route('/eval')
  def contents_dict():
      data_type = mime.guess_type(request.data)[0]
      if data_type == 'application/json':
          return json.loads(request.data.decode())
      else:
          raise ValueError('Invalid JSON received')