from flask import Flask, request, make_response, escape

app = Flask(__name__)


@app.route("/first_name")
def echo_name():
    """
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    """
    try:
        first_name = request.args.get("first_name")
        print(f"First name received: {first_name}")

        # Check if first_name is provided (to avoid KeyError)
        if not first_name or len(first_name) < 1:
            return make_response("Please provide your first name", 400)
    except ValueError as e:
        print(f"Error retrieving first name: {e}")
        return make_response("Error in retrieving first name", 500)

    # Greet the user by name
    greeting = f"Greetings, {first_name.strip()}!" if len(first_name) > 1 else "Hello!"
    print(f"Greeting: {greeting}")

    return make_response(escape(greeting), 200)
