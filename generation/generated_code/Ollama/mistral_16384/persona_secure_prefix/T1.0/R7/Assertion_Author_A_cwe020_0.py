 def match_string(target_string):
       return re.match(r'^[a-zA-Z0-9]+(\.[a-zA-Z0-9]+)*$', target_string) is not None

This function uses regular expressions to check if the input string matches the format 'x.y.z'. It returns True if it matches and False otherwise. The regular expression used here matches any sequence of alphanumeric characters (a-z, A-Z, 0-9) that can optionally be separated by dots ('\.'). The '^' character indicates the start of the string, '$' indicates the end, and '*' means zero or more occurrences.