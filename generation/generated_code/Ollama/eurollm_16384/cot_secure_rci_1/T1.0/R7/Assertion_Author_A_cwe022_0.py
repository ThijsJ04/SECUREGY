from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/deleteImage', methods=['GET'])
def deleteImage():
    image_path = request.args.get('path')
    if image_path:
        # Check if the file exists and is a valid image
        file_exists, file_type = os.path.isfile(image_path) and os.path.splitext(image_path)[1] in ['.png', '.jpg', '.jpeg']
        if file_exists:
            try:
                os.remove(image_path)
                success_message = "The file has been deleted"
            except Exception as e:
                success_message = f"An error occurred: {e}"
        else:
            success_message = "The file does not exist"
    else:
        success_message = "No image path provided in the request"

    return success_message