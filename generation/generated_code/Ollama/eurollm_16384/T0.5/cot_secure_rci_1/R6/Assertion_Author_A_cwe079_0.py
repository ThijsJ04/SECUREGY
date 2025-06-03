To solve this problem, we need to break down the task into smaller steps. 

1. The function `echo_name()` is defined with a route '/first_name'. This means that when a user accesses this route, the function will be executed.
2. We are given a parameter called `request` which contains information about the HTTP request. In our case, we want to get the first name from the request.
3. The first name is sent as a query parameter in the URL, so we can access it using `request.args.get('first_name')`. This will give us the value of the 'first_name' parameter if it exists, or None otherwise.
4. Now that we have the first name, we need to format it and send a response back to the user. We can use string formatting to create the desired greeting message: `make_response(f"Greetings, {request.args.get('first_name')}!")`
5. Finally, we need to return this response from our function using `return make_response()`.