@app.route('/eval', methods=['POST'])
def eval_contents():
    data = request.get_json()
    file_contents = data.get("file_contents")

    if file_contents:
        # Remove anything before the first '{' and after the last '}'
        start_index = file_contents[0].find('{') + 1
        end_index = len(file_contents) - file_contents[-1].rfind('}')
        evaluated_data = eval(file_contents[start_index:end_index])
    else:
        evaluated_data = None

    return evaluated_data