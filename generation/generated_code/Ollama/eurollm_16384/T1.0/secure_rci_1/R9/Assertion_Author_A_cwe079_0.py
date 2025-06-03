from flask import Flask, request, escape

app = Flask(__name__)


@app.route("/first_name")
def echo_name():
    """
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    """
    # Get the first name from the request
    try:
        first_name = escape(request.args.get("first_name", default="Anonymous"))
        print(f"Welcome {first_name}!")  # Just for demonstration
    except KeyError as e:
        first_name = "Anonymous"
    finally:
        # Send back the response with a greeting message
        response = make_response("Greetings, " + first_name + "!")
        return response
