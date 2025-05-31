@app.route('/img/upload')
def upload_img():
    filename = request.args.get('filename', '')
    img = request.args.get('img', None)
    if img is not None and len(img) > 0:
        with open(f'../assets/img/{filename}.png', 'wb') as f:
            f.write(base64.b64decode(img))
    return Response(status=200)