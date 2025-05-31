@app.route('/lookup')
def lookup():
   # Get the input from the request and store them in variables regex and data
   regex = request.args.get('regex', default='')
   data = request.args.get('data', default='').split(', ') 

    # Remove leading/trailing spaces from data using re.sub() function
   clean_data = [re.sub('^ *|\s$', '', d) for d in data] 
       # Check if regex exists in the data
   result = False 

    # Searching through each line of data 
   for line in clean_data: 
        # Check using re.search() 
        if (re.search(regex, line)): 
            result = True
            break
           # Return "Match found" if regex exists, otherwise return "No match found"   
   return "Match found" if result else "No match found"