from flask import Flask, request, make_response, escape

app = Flask(__name__)

@app.route('/first_name')
def echo_name():
    # Get the first name from the request using 'first_name'
    data = request.args.get('first_name')

    if not data:
        return make_response(f"Sorry, no value for 'first_name'", 400)

    # Convert first name to title case
    first_name = data[0].upper() + data[1:]

    # Send back the greeting message with the user's first name
    return make_response(f"Greetings, {escape(first_name)!r}!", 200)

if __name__ == '__main__':
    app.run(debug=True)