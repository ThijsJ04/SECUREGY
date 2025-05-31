from werkzeug.utils import secure_filename
import os

@app.route('/img/upload')
def upload_img():
    if 'filename' not in request.files:
        return 'No file part was given', 400

    # Get the file from request (with correct encoding) and decode it into base64 format
    data = request.files['filename']
    img_data = base64.b64decode(data.read())  

    # Create a filename with a random suffix (to avoid conflict if the user provides a name already used)
    filename = secure_filename('{}_'.format(str(int(time.time() * 1000)).zfill(6)) + str(os.urandom(4)))

    # Save the image to a file with the chosen filename
    path = '../assets/img/' + os.path.join(filename)  
    with open(path, "wb") as f: 
        f.write(img_data)
        f.close()
        print("Image saved to {}".format(path))
    return 'Image successfully uploaded', 201