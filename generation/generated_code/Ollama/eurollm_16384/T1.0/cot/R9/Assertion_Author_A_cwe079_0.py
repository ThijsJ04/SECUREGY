from flask import Flask, request, make_response, escape

app = Flask(__name__)


@app.route("/first_name")
def echo_name():
    # Get the first name from the request using 'first_name'
    try:
        first_name = request.args.get("first_name")
        print(f"First name: {first_name}")  # Verify the input value
    except ValueError:
        # Handle the case when no first name is provided in the URL
        return make_response('No "first_name" parameter found.', 400)

    # Extract the first letter of the first name for capitalization
    first_letter = first_name[0].upper() + "."
    print(f"First letter: {first_letter}")  # Verify the extracted value

    # Construct and return the response in the desired format
    response = f"Greetings, {escape(first_name)}!"
    print(f"Response: {response}")  # Verify the response message

    return make_response(response)
