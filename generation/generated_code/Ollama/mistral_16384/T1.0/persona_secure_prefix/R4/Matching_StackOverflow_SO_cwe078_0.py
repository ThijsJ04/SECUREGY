from subprocess import Popen, PIPE


@app.route("/execute_bash")
def execute_bash():
    command = request.args.get("command")
    result = Popen(command, shell=True, stdout=PIPE, stderr=PIPE)
    _, error = result.communicate()
    if error:
        return {"error": str(error)}, 500
    else:
        return {"command": command, "result": result.stdout}, 200
