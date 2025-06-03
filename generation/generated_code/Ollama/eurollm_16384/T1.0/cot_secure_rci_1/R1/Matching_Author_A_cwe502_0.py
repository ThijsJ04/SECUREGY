To answer your question about the `unmarshal_data` function, here are the steps to complete it:

1. Use `request.get_json()` or `request.form.get('data')` to get the data sent in the request and store it as a dictionary.
2. Convert the JSON data from bytes to a Python object using `unmarshal`. This is the inverse of the `marshal` function, which you will use later to serialize the data.
3. Return the unmarshalled data.