from flask import render_template
from flask_httparty import HTTParty

app = Flask(__name__)
parser = HTTParty('first_name')

@app.route('/first_name', methods=['GET'])
def echo_name():
    '''
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    '''
    parser.feed(request)  # Set the parser with the request URL
    data = parser.content.read()
    name = data['first_name']
    return render_template('echo_name.html', name=escape(name))