import os
from io import BytesIO

...

@app.route('/img/upload')
def upload_img():
    filename = request.args.get('filename')
    img_b64 = request.form['img']

    img_data = base64.decodebytes(img_b64)
    img_file = BytesIO(img_data)

    filepath = os.path.join("../assets/img", f"{filename}.png")
    with open(filepath, "wb") as out_file:
        out_file.write(img_file.getvalue())

    return Response(status=200)