@app.route('/eval', methods=['POST'])
def eval_request():
    file_contents = request.form['file_contents']
    data = {}  # Initialize an empty dictionary to store the evaluated content

    for line in file_contents.splitlines():
        if '{' not in line:  # Skip lines without a '{' character
            continue
        start_pos = line.find('{') + 1  # Find the position of the first '{'
        end_pos = len(line) - line[-1:]  # Find the position of the last '}'
        content = line[start_pos:end_pos]  # Extract the content between '{' and '}'

        if not content.strip():  # Skip empty lines or lines with only whitespace
            continue

        try:
            value = eval(content)  # Evaluate the content as a Python expression
            data[line.split('}')[-1]] = value  # Store the evaluated value in the dictionary
        except Exception as e:
            print(f"Error evaluating {content}: {str(e)}")
            return "Invalid input", 500

    if not data:  # Return an empty dictionary if no content was found
        data = {}

    return str(data)  # Return the evaluated dictionary as a JSON-formatted string