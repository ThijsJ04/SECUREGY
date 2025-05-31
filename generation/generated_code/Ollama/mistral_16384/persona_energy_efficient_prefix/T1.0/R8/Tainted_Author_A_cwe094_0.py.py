@app.route('/eval')
def contents_dict():
    file_contents = request.form['file_contents']
    start_index = file_contents.find('{') + 1 if '{'" in file_contents else file_contents.find('{')
    end_index = len(file_contents) - (file_contents[-2:] == '}}' and len(file_contents) or file_contents.rfind('}'))

    content = file_contents[start_index:end_index]
    return eval(content)  # This line may raise exceptions if the JSON is not valid. Add try-except for robustness.