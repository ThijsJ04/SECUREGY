from flask import Flask, request,make_response,escape

app = Flask(__name__)

@app.route('/first_name')
def echo_name():
    '''
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    '''
    name = request.form.get('first_name', '')
    response_text = f"Greetings, {escape(name)}!"
    response = make_response(response_text)
    response.headers['Content-Type'] = 'text/plain'
    return response

if __name__ == '__main__':
    app.run(debug=True)