from flask import make_response, abort

@app.route('/eval')
def contents_dict():
    data = request.get_json()
    if not data or 'file_contents' not in data:
        abort(400)  # Bad request
        return "Invalid data sent"

    result = eval(data['file_contents'])

    return make_response("{" + str(result) + "}", 200)