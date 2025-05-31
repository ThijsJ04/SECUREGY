from flask import Flask, request,make_response,escape

app = Flask(__name__)

@app.route('/first_name')
def echo_name():
    name = request.form.get('first_name', 'Guest')
    escaped_name = escape(name)
    greeting = f'Greetings, {escaped_name}!'
    return make_response(greeting, 200, {'Content-Type': 'text/plain'})

if __name__ == '__main__':
    app.run(debug=True)