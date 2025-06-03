To create this Flask application, you need to follow these steps:

1. Import the necessary modules and libraries: `Flask` for creating the web application, `request` to access the incoming request data, `Response` to send a response back to the client, `base64` for decoding the image file, and `__name__` to determine the current module's name.

2. Create an instance of Flask class called `app`.

3. Define a route using the `@app.route()` decorator. In this case, we will use '/img/upload'. This route will be used to handle image uploads.

4. Inside the route function (`upload_img()`), access the "filename" from the request using `request.form['filename']` and "img" parameter using `request.data`.

5. Use base64 encoding/decoding to convert the image data into a string, then decode it back to its original format.

6. Save the decoded image to an asset file named after the filename with '.png' extension in the 'assets/img' directory using `with open('../assets/img/{filename}.png', 'wb') as f:`. The `wb` argument stands for write binary, which is required when working with image files.

7. Return a response object with HTTP status code 200 (indicating successful execution) using `return Response(status=200)`.