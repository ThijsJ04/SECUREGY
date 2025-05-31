from flask import Flask, request, make_response, escape
app = Flask(__name__)

@app.route('/first_name')
def echo_name():
    first_name = request.args.get("first_name") # assuming the first name is provided as a query parameter
    content = "Greetings, " + escape(first_name).strip() + "!"
    response = make_response(content)
    return response