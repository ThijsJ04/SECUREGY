@app.route('/img/upload')
def upload_img():
    data = request.data
    filename = request.args.get('filename')  # Get the "filename" from the request
    if filename is None:
        return 'Error: Missing "filename" parameter', 400

    # Encode the image to base64
    data_base64 = base64.b64encode(data).decode('utf-8')  # Decode the encoded data

    # Save the image to the file "../assets/img/{filename}.png"
    with open(f'../assets/img/{filename}.png', 'wb') as f:
        f.write(data_base64)  # Write the base64 encoded image data to the file

    return Response('Image uploaded successfully!', status=200, mimetype='application/json')