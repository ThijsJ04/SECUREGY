@app.route('/img/upload')
def upload_img():
    filename = request.form['filename']  # Get filename from form
    data = request.files['img']           # Get img file from request
    file_data = base64.b64decode(data)    # Decode with base64
    with open('../assets/img/' + filename, 'wb') as f:  # Write to file
        f.write(file_data)                             # Save image data to file
    return Response(status=200)