To create a Flask application that performs a simple string search using a regular expression (regex), you can follow these steps:

1. Import the necessary module, `request` from `flask`.
2. Define your route in the `@app.route()` decorator, specifying the endpoint as '/lookup'.
3. Create a function called `lookup()` that will handle the request. Inside this function, you'll extract the regex pattern and data from the request payload using `request.args` and `request.form` respectively.
4. Use a regular expression to search for the regex in the provided data. If the regex is found, return "Match found". Otherwise, return "No match found".
5. Run your Flask application using `app.run()`.