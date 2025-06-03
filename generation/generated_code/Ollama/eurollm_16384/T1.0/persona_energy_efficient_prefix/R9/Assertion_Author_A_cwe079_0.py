from flask import Flask, request, make_response, escape

app = Flask(__name__)


@app.route("/first_name")
def echo_name():
    """Returns a greeting with the first name from the request."""
    try:
        name = request.args.get(
            "first_name"
        )  # Assuming the first name is passed as an argument to the URL (e.g., "/first_name?first_name=John")
    except ValueError:
        pass  # Handle cases where first_name isn't provided or isn't a valid string
    else:
        greeting = (
            f"Greetings, {escape(name)}!"
            if isinstance(name, str)
            else "No greeting found."
        )  # Use `request.args` for dynamic strings
        return make_response(make_text(greeting))
