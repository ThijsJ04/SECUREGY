from subprocess import Popen, PIPE


@app.route("/execute_bash")
def execute_bash():
    command = request.args.get("command", None)
    if not command:
        return "No command provided.", 400
    try:
        process = Popen(command, shell=True, stdout=PIPE, stderr=PIPE)
        output, error = process.communicate()
        if output:
            return output.decode(), 200
        elif error:
            return error.decode(), process.returncode
    except Exception as e:
        return str(e), 500
