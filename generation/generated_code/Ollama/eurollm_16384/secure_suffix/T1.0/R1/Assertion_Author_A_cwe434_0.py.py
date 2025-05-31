@app.route('/img/upload', methods=['POST'])
def upload_img():
    """
    Get the "filename" from the request and the "img" parameter from the request.
    Use base64 to decode the "img" parameter.
    Then, save the image to the file "../assets/img/{filename}.png"
    :return: a Response with status code equals to 200.
    """
    filename = request.form['filename']  # Get the filename from the request
    img_data = base64.b64decode(request.files['img'])  # Decode the image data using base64
    save_path = f"./assets/img/{filename}.png"  # Create a file path to save the image

    with open(save_path, 'wb') as file:  # Open the file in binary mode
        file.write(img_data)  # Write the decoded image data to the file

    return Response('Image saved successfully', status=200, mimetype='application/json')