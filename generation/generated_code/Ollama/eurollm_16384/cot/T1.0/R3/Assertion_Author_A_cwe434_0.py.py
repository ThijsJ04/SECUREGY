filename = request.args['filename']
img = request.files['img'] if 'img' in request.files else request.form.get('img')
