from flask import Flask, request

app = Flask(__name__)


@app.route("/first_name", methods=["GET"])
def echo_name():
    try:
        # Get the first name from the request using 'first_name' and convert it to lower case for consistency
        name = request.args.get("first_name").lower()
        # Send a response back to the user in the desired format
        return make_response(f"Greetings, {name}!", 200)
    except (
        Exception
    ) as e:  # Catch any exceptions that occur during the execution of this function
        # Return an error message if there is an exception
        return "An error occurred. Please try again later."
