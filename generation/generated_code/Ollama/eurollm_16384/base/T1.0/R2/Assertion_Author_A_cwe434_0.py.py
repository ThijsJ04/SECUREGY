from flask import Flask, request, Response
import base64

app = Flask(__name__)

@app.route('/img/upload')
def upload_img():
    # Get the "filename" from the request
    filename = request.args.get("filename") or "default_image"  # default filename if not provided

    # Get the "img" parameter from the request
    img_data = request.form["img"]  # assume img is a file field in form data

    # Decode the image using base64
    try:
        with open(f"./assets/img/{filename}.png", "wb") as f:
            f.write(base64.decodebytes(img_data))
        print("Image saved successfully!")
    except Exception as e:
        print(e)
        return Response("An error occurred while saving the image", status=500, mimetype="text/plain")  # return 500 with a generic error message

    # Return response with status code equals to 200
    return Response("Image saved successfully!", status=200)