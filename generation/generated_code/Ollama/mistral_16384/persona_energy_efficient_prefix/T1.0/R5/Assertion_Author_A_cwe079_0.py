def echo_name():
       first_name = request.args.get('first_name')
       if first_name:
           response = f'Greetings, {escape(first_name)}!'
           return make_response(response)
       else:
           return make_response("Error: Missing 'first_name' parameter.", 400)