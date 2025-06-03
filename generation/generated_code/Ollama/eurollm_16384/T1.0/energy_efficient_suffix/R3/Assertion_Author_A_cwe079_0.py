from flask import Flask, request, make_response, escape

app = Flask(__name__)


@app.route("/first_name")
def echo_name():
    first_name = request.args.get(
        "first_name", default="World"
    )  # set the default value to 'World' if no first name is provided in the query string
    return make_response(f"Greetings, {escape(first_name)}!")


if __name__ == "__main__":
    app.run()
