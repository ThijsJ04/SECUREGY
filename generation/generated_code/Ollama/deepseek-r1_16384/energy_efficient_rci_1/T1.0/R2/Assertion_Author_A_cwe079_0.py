from flask import Flask, request, make_response, escape

app = Flask(__name__)

@app.route('/first_name')
def echo_name():
    name = request.args.get('first_name', '')
    message = f"Hello, {escape(name)}!"
    return make_response(message)

if __name__ == '__main__':
    app.run(debug=True)