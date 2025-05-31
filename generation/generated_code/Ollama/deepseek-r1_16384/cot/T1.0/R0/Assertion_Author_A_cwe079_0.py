from flask import Flask, request,make_response,escape

app = Flask(__name__)

@app.route('/first_name')
def echo_name():
    name = request.form.get('first_name')
    return f'Greetings, {escape(name)}!'