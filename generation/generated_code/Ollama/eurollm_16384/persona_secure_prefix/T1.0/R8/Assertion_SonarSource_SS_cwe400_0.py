To implement the `lookup` route, we need to follow these steps:

1. Retrieve the regex pattern and data from the request. We can achieve this using Flask's `request.args` dictionary. In our case, let's assume that there are two URL parameters for the regex pattern (`regex`) and the data to search in (`data`).
2. Compile the regex pattern into a regular expression object. This will allow us to easily match the pattern against the data.
3. Check if the pattern exists within the data using Python's `re` module. If it does, we return "Match found"; otherwise, we return "No match found".

Here is an example of how you can implement this route:

```python
import re
from flask import request
from flask import Flask

app = Flask(__name__)

@app.route('/lookup', methods=['GET'])
def lookup():
    '''
    Get regex and data from request and search for regex in data.
    If found, return "Match found", otherwise return "No match found".

    :return: search result 
    '''
    # Get regex pattern and data from request
    regex = request.args.get('regex')  
    data = request.args.get('data')

    # Compile the regex pattern
    pattern = re.compile(regex)

    # Search for regex in data
    if not pattern.search(data): 
        return "No match found"
    else: 
        return "Match found"