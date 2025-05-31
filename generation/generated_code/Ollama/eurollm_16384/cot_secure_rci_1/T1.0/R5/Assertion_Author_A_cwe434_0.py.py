@app.route('/img/upload')
def upload_img():
    filename = request.url_path
    try:
        img_data = request.files.get('image').read()  # get the image data from the request
        encoded_bytes = base64.b64decode(img_data)  # decode the image bytes using base64
        with open(f'../assets/img/{filename}.png', 'wb') as file:
            file.write(encoded_bytes)  # save the image to a file named after the filename
    except Exception as e:
        print('Error:', str(e))
    finally:
        return Response(status=200, mimetype='application/json')  # return a JSON response with 'success' status code