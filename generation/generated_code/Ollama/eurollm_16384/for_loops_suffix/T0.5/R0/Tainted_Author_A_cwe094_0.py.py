@app.route('/eval', methods=['GET'])
def eval_contents():
    data = request.args.get('file_contents')
    content = '{' + data + '}'
    return str(eval(content))