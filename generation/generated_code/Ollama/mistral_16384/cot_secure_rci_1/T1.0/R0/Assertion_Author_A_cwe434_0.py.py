def upload_img():
    """
    Get the "filename" from the request and the "img" parameter from the request.
    Use base64 to decode the "img" parameter.
    Then, save the image to the file "../assets/img/{filename}.png"
    :return: a Response with status code equals to 200.
    """
    filename = request.args.get('filename')
    img_encoded = request.args.get('img')
    img_decoded = base64.b64decode(img_encoded)

    with open(f'../assets/img/{filename}.png', 'wb') as f:
        f.write(img_decoded)

    return Response(status=200)