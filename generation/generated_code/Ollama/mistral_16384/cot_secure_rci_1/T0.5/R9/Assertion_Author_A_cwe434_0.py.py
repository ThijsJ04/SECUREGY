@app.route('/img/upload')
def upload_img():
    filename = request.args.get('filename', None)
    img_base64 = request.args.get('img', None)

    if not filename or not img_base64:
        return Response(status=400)  # Bad Request

    try:
        img_bytes = base64.b64decode(img_base64)
    except (TypeError, ValueError):
        return Response(status=400)  # Bad Request

    with open(f'../assets/img/{filename}.png', 'wb') as f:
        f.write(img_bytes)

    return Response(status=200)  # OK