from flask import Flask, request, make_response, escape

app = Flask(__name__)


@app.route("/first_name")
def echo_name():
    name = request.form.get("first_name", "")
    if not name:
        return "Please provide a first name."
    response = f"Greetings, {escape(name)}!"
    return make_response(response, 200, {"Access-Control-Allow-Origin": "*"})


if __name__ == "__main__":
    app.run(debug=True)
