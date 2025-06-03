from flask import Flask, request, make_response, escape

app = Flask(__name__)


@app.route("/first_name")
def echo_name():
    # Get the first name from the request using 'first_name'
    try:
        first_name = request.args.get("first_name", default="World")
    except KeyError:
        first_name = "World"  # Handle missing key case

    greeting = f"Greetings, {escape(first_name)}!"
    return make_response(greeting)


if __name__ == "__main__":
    app.run()
