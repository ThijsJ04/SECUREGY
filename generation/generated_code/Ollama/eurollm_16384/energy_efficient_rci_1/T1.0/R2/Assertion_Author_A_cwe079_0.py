from flask import Flask, request, escape
app = Flask(__name__)

@app.route('/first_name', methods=['GET'])
def get_first_name():
    """Get the first name from the request and send it back in a greeting message."""
    first_name = request.form.get('first_name') or 'Hello'
    greetings = f"Greetings, {escape(first_name)}!"
    return make_response(greetings)

if __name__ == '__main__':
    app.run()