import os
from io import BytesIO
import base64

@app.route('/img/upload')
def upload_img():
    filename = request.args.get('filename', '')
    img_str = request.form['img']
    img_data = base64.b64decode(img_str)
    img_file = BytesIO(img_data)
    filepath = os.path.join("../assets/img", f"{filename}.png")
    with open(filepath, 'wb') as f:
        f.write(img_file.getvalue())
    return Response(status=200)