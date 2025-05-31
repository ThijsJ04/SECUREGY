import os

@app.route('/img/upload')
def upload_img():
    filename = request.args.get('filename', '')
    img_data = base64.b64decode(request.form['img'])
    with open(os.path.join('../assets/img/{}.png'.format(filename), 'wb') as f:
        f.write(img_data)
    return Response(status=200)