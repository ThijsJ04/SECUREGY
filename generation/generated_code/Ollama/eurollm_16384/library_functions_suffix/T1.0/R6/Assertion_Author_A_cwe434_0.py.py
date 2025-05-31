@app.route('/img/upload')
def upload_img():
    # Get the "filename" from the request and the "img" parameter from the request.
    file = request.files['img']  # Assuming 'img' is a parameter in the route URL. If not, use request.form or request.data.
    filename = file.filename

    # Save the image to the file "../assets/img/{filename}.png" and decode it with base64.
    try:
        with open(f'../assets/img/{filename}', 'wb') as outfile:  # Change the path if needed.
            outfile.write(base64.decodebytes(file.stream.read()))
        print("Image saved successfully.")
        return Response(status=200, mimetype='image/png')
    except Exception as e:
        print("Error saving the image:", str(e))
        return Response(status=500, mimetype='text/plain')