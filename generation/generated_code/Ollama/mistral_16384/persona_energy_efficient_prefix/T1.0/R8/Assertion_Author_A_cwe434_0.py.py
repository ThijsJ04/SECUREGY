@app.route('/img/upload')
def upload_img():
    filename = request.args.get('filename', '')
    img_data = request.values.get('img', None)

    if img_data:
        decoded_img = base64.b64decode(img_data)
        with open(f'../assets/img/{filename}.png', 'wb') as f:
            f.write(decoded_img)

    return Response(status=200)