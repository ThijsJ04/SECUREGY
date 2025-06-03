from PIL import Image

img_bytes = base64.b64decode(img)  # decoded image bytes
img_data = Image.open(BytesIO(img_bytes))  # open the image data as an image object
img_data.save(
    "../assets/img/{filename}.png".format(filename=request.form["filename"])
)  # save the image to a file
