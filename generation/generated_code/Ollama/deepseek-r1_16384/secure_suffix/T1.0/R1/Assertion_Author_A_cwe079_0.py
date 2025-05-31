from flask import Flask, request, make_response, escape

app = Flask(__name__)

@app.route('/first_name')
def echo_name():
    name = request.args.get('first_name', 'Guest')
    greeting = f'Greetings, {escape(name)}!'
    return make_response(greeting)

if __name__ == "__main__":
    app.run(debug=True)