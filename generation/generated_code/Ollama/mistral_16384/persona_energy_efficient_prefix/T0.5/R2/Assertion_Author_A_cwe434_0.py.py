@app.route('/img/upload')
def upload_img():
    filename = request.args.get('filename', None)
    img_b64 = request.args.get('img', None)

    if not all([filename, img_b64]):
        return Response('Missing parameters', status=400)

    with open(f"../assets/img/{filename}.png", "wb") as f:
        img = base64.b64decode(img_b64)
        f.write(img)

    return Response('Image saved successfully', status=200)