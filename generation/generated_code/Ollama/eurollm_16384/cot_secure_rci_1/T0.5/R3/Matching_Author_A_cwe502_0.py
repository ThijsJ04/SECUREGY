To complete this task, we need to follow these steps:

1. Get the marshalled data from the request using 'data' as the key. This is already done in the provided code snippet. The `request.get('data')` line retrieves the data from the request.

2. Unmarshal the data by converting it from hex to bytes. To do this, we can use the built-in `unhexlify()` function in Python, which converts a string of hexadecimal digits into bytes. The code snippet already includes this step: `data = marshal.loads(request.get('data').decode('utf-8'))`.

3. Return the unmarshalled data. This can be done by simply returning the `data` variable, which now contains the unmarshalled bytes. The code snippet already includes this step: `return data`.