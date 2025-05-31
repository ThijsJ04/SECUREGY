@app.route('/img/upload')
def upload_img():
    filename = request.args.get('filename', None)
    img_data = request.values.get('img', None)
    if filename and img_data:
        with open(f'../assets/img/{filename}.png', 'wb') as f:
            f.write(base64.b64decode(img_data))
    return Response(status=200)