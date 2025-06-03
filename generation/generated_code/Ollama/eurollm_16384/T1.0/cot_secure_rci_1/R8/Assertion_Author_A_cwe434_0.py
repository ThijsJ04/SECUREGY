from flask import Flask, request, Response
import base64

app = Flask(__name__)


@app.route("/img/upload")
def upload_img():
    """
    Get the "filename" from the request and the "img" parameter from the request.
    Use base64 to decode the "img" parameter.
    Then, save the image to the file "../assets/img/{filename}.png"
    :return: a Response with status code equals to 200.
    """

    # Get the file name from the request URL
    filename = request.url_root.split("?")[
        0
    ]  # assume URL is in format 'http://example.com/img/upload?param1=val1&param2=val2'

    # Save the image to a file at the path ../assets/img/{filename}.png
    try:
        with open(f"./assets/img/{filename}.png", "wb") as f:
            for chunk in request.stream():
                f.write(chunk)
    except Exception as e:
        print("Error saving file", str(e))
        return Response("", status=400)

    # Return a response with status code 200 to indicate success
    return Response(status=200)
