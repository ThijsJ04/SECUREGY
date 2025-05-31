@app.route('/img/upload')
def upload_img():
    filename = request.form['filename']  # or get filename from request
    data = request.files['img']            # get image parameter

    encoded_data = base64.b64decode(data)
    with open(f'../assets/img/{filename}.png', 'wb') as f:
        f.write(encoded_data)

    return Response('Image saved successfully!', status=200, mimetype='text/plain')