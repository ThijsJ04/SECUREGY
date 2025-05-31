@app.route('/img/upload', methods=['POST'])
def upload_img():
    data = request.files['file']
    filename = str(data.filename)
    if not filename:
        return 'No file name provided', 400
    with open('../assets/img/{}.png'.format(filename), 'wb') as f:
        data.save(f)
    print("Image saved successfully")
    response = Response(mimetype='image/png')
    return response