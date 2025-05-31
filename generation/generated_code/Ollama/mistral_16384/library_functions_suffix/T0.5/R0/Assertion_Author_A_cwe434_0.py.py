@app.route('/img/upload')
def upload_img():
    filename = request.args.get('filename', None)
    img_data = base64.b64decode(request.form['img'])

    with open(f'../assets/img/{filename}.png', 'wb') as f:
        f.write(img_data)

    return Response(status=200)