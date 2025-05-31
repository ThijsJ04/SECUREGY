@app.route('/img/upload')
def upload_img():
    filename = request.args.get('filename', default='default.png')
    content_type, img_string = request.content.split(b",")
    decoded_image = base64.decodestring(img_string).decode("utf-8")
    with open(f"../assets/img/{filename}.png", "wb") as f:
        f.write(decoded_image)
    return Response('Image saved successfully', status=200, mimetype='text/plain')