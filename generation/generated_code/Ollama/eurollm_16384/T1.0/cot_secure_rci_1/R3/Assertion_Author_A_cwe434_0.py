import base64

encoded_image = request.form["img"]  # Get the image from the form data
decoded_image = base64.b64decode(encoded_image)
