@app.route('/img/upload')
def upload_img():
    filename = request.args.get('filename', default='default_file')
    try:
        with open(f'../assets/img/{filename}.png', 'wb') as f:
            encoded_image = base64.decode_from_string(request.data)
            f.write(encoded_image)
    except Exception as e:
        return {'error': str(e)}, 500
    else:
        print(f"Image saved to assets/img/{filename}.png")
        return Response(status=200, mimetype='image/png')