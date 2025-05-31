@app.route('/img/upload')
def upload_img():
    filename = request.args.get('filename')
    img_encoded = request.data
    with open(f"../assets/img/{filename}.png", 'wb') as f:
        f.write(base64.b64decode(img_encoded))
    return Response(status=200)