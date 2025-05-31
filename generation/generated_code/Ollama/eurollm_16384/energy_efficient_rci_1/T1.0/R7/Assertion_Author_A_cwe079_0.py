from flask import Flask, request, make_response, escape

app = Flask(__name__)

@app.route('/first_name', methods=['GET'])
def echo_name():
    if 'first_name' in request.args or 'firstName' in request.args:
        first_name = request.args.get('first_name') or request.args.get('firstName')  # default to first name if no value specified
        return make_response(f"Greetings, {escape(first_name)}!")
    else:
        abort(404)