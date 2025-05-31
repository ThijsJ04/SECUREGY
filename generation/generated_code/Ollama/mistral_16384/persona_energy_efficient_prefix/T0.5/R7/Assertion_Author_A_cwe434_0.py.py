@app.route('/img/upload')
def upload_img():
    filename = request.args.get('filename', None)
    img_str = request.args.get('img', None)

    if not filename or not img_str:
        return Response(status=400)

    with open(f'../assets/img/{filename}.png', 'wb') as f:
        f.write(base64.b64decode(img_str))

    return Response(status=200)