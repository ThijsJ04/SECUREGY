def execute_bash():
    command = request.args.get('command')
    if command:
        os.system(command)
    return command