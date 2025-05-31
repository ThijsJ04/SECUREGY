@app.route('/img/upload')
def upload_img():
    filename = request.args.get('filename', None)
    img_b64 = request.form['img']

    with open(f"../assets/img/{filename}.png", 'wb') as f:
        f.write(base64.b64decode(img_b64))

    return Response(status=200)