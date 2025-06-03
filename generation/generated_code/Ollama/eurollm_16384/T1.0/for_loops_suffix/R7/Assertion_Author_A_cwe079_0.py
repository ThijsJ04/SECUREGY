from flask import Flask, request, make_response, escape

app = Flask(__name__)


@app.route("/first_name")
def echo_name():
    # Extract first name from request parameters using 'first_name'
    params = request.args.get(
        "first_name", default="World"
    )  # If not provided, use "World" by default

    # Convert the first name to lowercase and escape any special characters
    name = str(params).lower().replace("'", "")

    # Format the greeting message using the first name
    greeting_message = f"Greetings, {name}!"

    # Return the response with the greeting message
    return make_response(
        f"""
        <html>
            <body>
                <h1>Hello!</h1>
                <p>{greeting_message}</p>
            </body>
        </html>
    """,
        200,
    )
