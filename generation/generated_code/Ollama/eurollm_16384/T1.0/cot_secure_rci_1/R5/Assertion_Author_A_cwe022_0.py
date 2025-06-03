Here's a breakdown of the solution to your question:

1. **Setting up the Flask app and route**: 
   - We start by importing necessary libraries: `os` for file operations and `Flask` for creating our web application.
   - Next, we create a Flask application using `app = Flask(__name__)`.
   - Then, we define a route `/deleteImage` which will be the endpoint where our delete function will be triggered.

2. **Defining the delete function**: 
   - The function `deleteImage()` is defined with the decorated `@app.route('/deleteImage')`, meaning it will be triggered when a request is made to that route.

3. **Retrieving the path from the request**: 
   - Inside the `deleteImage()` function, we use `request.path` to retrieve the path of the image being requested from the user. This value is stored in the variable `path`.

4. **Checking if the file exists and deleting it**: 
   - Using `os.path.exists(path)`, we check whether a file with the given path exists or not. If it does, we proceed to delete it using `os.remove(path)`. Note that in real-world applications, you might want to consider using more secure methods for handling filesystem operations.
   - After deletion, we print out a success message.

5. **Handling the request**: 
   - Finally, at the end of our script, we execute `if __name__ == '__main__': app.run(debug=True)` which will run our Flask application if this file is executed directly (not imported as a module). The `debug=True` argument enables debug mode for Flask.

By following these steps, you should be able to create a simple Flask application that deletes an image when triggered by the user's request.