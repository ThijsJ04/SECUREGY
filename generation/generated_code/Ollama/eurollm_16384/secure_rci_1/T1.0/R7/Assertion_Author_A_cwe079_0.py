from flask import Flask, request, make_response, escape

app = Flask(__name__)

@app.route('/first_name', methods=['GET'])
def echo_name():
    # Get the first name from the request using 'first_name'
    first_name = request.args.get("first_name", default="John")  # Add your actual request variable if needed
    print(first_name)  # You can remove this line in a real application

    # Send the greeting back to the user
    return make_response(f'Greetings, {escape(first_name)}!', 200)