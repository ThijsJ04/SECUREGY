@app.route('/img/upload')
def upload_img():
    """Uploads an image and saves it in the '../assets/img' directory."""
    try:
        filename = request.args.get("filename")
        if not filename:
            return "Error: Missing 'filename' parameter", 400
    except ValueError:
        print("Error: Invalid filename provided.")
        return "Error: Invalid filename provided. Please provide a valid filename.", 500

    try:
        img = request.files['img']
        if not img:
            return "Error: Missing 'img' parameter or empty file upload."
    except KeyError:
        print("Error: No 'img' parameter found in request.")
        return "Error: No 'img' parameter found. Please include an image for uploading.", 500

    with open(f"../assets/img/{filename}.png", "wb") as img_file:
        img.save(img_file)

    return Response("Image saved successfully!", mimetype='image/png')