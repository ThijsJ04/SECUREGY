# Create an instance of the Flask application.
app = Flask(__name__)

# Define a route that will execute a Bash command based on the input from the user.
@app.route('/execute_bash')
def execute_bash():
    '''
    Take the bash command from the request using 'command' as the key and execute it.
    Return the command.
    '''
    command = request.headers.get('command', None) # Get the Bash command from the headers.
    if not command:
        return 'Error: No command specified.'
    # Execute the command using subprocess.run().
    result = subprocess.run(command, shell=True, capture_output=True, text=True) # Run the Bash command and store its output in a string variable called result.
    return 'Command executed successfully: ' + result