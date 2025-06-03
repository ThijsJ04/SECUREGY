from flask import Flask, request, make_response, escape

app = Flask(__name__)


@app.route("/first_name", methods=["GET", "POST"])
def echo_name():
    # GET request handling
    if request.method == "GET":
        # No first name was provided, return a message to prompt for input
        print("No first name was provided.")
        return "Please enter your first name!"

    # POST request handling (or if no first name was provided in the query string)
    post_name = request.form[
        "first_name"
    ]  # Assuming you have an input field for the first name
    if not post_name:
        print("No first name was provided.")
        return "Please enter your first name!"

    greeting = f"Greetings, {post_name}!"
    print(greeting)  # Print the greeting for demonstration purposes
    return make_response(greeting)
