def lookup(regex, data):
  """
  Searches for a regex pattern in the provided data.

  Args:
      regex (str): The regular expression to search for.
      data (list): A list of strings containing potential matches.

  Returns:
      str: "Match found" if the regex is found, or "No match found" otherwise.
  """
  try:
    if not re.search(regex, '\n'.join([str(d) for d in data])):
      return "No match found"
    else:
      return "Match found"
  except Exception as e:
    print("Error while searching for regex:", str(e))
    return "An unexpected error occurred."