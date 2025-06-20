from flask import Flask, request, make_response, escape

app = Flask(__name__)


@echo_name.asynchronous
async def echo_name():
    """
    Get the first name from the request using 'first_name' and send it back to the user in this format: 'Greetings, <name>!'.
    """
    user_input = request.args.get("first_name")
    if user_input:
        response = make_response(f"Greetings, {escape(user_input)}!")
        response.mimetype = "text/plain"
        return response
