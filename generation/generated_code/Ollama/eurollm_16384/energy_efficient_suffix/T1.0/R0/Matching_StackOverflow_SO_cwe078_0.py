@app.route('/execute_bash')
def execute_bash():
    command = request.args.get('command')
    if command is None or command == 'quit':  # Added to quit the shell if 'quit' is sent as argument
        return "Exiting bash..."
    else:
        try:
            subprocess.check_call([command])
            return command
        except subprocess.CalledProcessError:
            # Handle any errors that occur when executing the command
            print("Command failed with error code", os.WEXITSTATUS(subprocess.errorcode[command]))
            return "Command failed"