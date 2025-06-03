from flask import Flask, request, make_response, escape

app = Flask(__name__)


@app.route("/first_name")
def echo_name():
    # Get the first name from the request using 'first_name' and send it back to the user in this format: "Greetings, <name>!"
    try:
        first_name = escape(request.args.get("first_name", default="Guest"))
        print("First Name:", first_name)
    except KeyError as e:
        print(
            e
        )  # Handle error if 'first_name' parameter is not provided in the request URL or query string
        first_name = "Guest"
    data = {"first_name": first_name}
    return make_response("Greetings, {}!".format(first_name), 200)
