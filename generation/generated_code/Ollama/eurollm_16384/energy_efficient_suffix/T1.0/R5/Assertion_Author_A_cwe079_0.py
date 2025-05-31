from flask import Flask, request, escape
app = Flask(__name__)

@app.route('/first_name')
def echo_name():
    name = escape(request.args.get("first_name"))  # get the first name from the 'first_name' query parameter
    return f"Greetings, {name}!"  # send back the greeting with the provided name

if __name__ == "__main__":
    app.run()