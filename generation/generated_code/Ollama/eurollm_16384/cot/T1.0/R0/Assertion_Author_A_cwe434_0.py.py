import base64
from flask import Response

def upload_img():
    filename = request.form['filename'] if 'filename' in request.form else None
    print(filename)  # You can check the filename here

    if filename:
        with open(f'./assets/img/{filename}.png', 'wb') as f:
            for chunk in request.data.split(b'\n'):
                f.write(chunk)  # Write chunks to file, assuming file is split into chunks for some reason
        return Response('Image saved successfully!', status=200)
    else:
        return Response('Filename not provided or invalid', status=400)