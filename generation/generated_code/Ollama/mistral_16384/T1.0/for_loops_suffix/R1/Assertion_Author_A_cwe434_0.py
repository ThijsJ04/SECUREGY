from flask import Flask, request, Response, jsonify
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
    if "img" not in request.json or not request.is_json:
        return jsonify({"error": "Invalid input format"}), 400

    img_data = request.json["img"]
    try:
        img_bytes = base64.b64decode(img_data)
    except (TypeError, ValueError):
        return jsonify({"error": "Invalid Base64 encoded data"}), 400

    if not img_bytes:
        return jsonify({"error": "Empty image data"}), 400

    filename = request.json.get("filename", f"img_{int(time.time())}.png")
    with open(f"../assets/img/{filename}", "wb") as f:
        f.write(img_bytes)

    return Response(status=200)
