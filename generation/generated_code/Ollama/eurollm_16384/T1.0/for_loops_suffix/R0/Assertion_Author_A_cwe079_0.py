from flask import Flask, request, make_response, escape

app = Flask(__name__)


@app.route("/first_name", methods=["POST"])
def echo_name():
    data = request.get_json()  # Assuming the JSON payload includes 'name': 'first name'
    if not data:
        return make_response("No data provided.", 400)

    name = data["name"]
    return make_response(f"Greetings, {escape(name)}!")
