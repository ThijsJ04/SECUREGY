To solve this problem, we need to break it down into steps. First, we import the necessary modules: `os` and `flask`. Then, we create a Flask app instance. Next, we define an endpoint for deleting images at '/deleteImage'. 

Inside the `deleteImage()` function, we check if the request path contains 'path' using `request.args.get('path')` and assign it to `path`. We then use `os.remove(path)` to delete the file at that path in the current directory. 

Finally, we return a message indicating whether the file was deleted or not. If the file exists and is successfully deleted, we return "The file has been deleted". Otherwise, we return "The file does not exist".