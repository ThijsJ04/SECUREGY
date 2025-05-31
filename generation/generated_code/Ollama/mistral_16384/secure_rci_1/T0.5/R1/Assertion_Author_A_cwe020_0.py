 def match_string(target_string):
       return re.match(r'^[a-zA-Z0-9]+(\.[a-zA-Z0-9]+){2}$', target_string) is not None

This function uses a regular expression to check if the input string matches the desired format (x.y.z). The regular expression `^` and `$` anchor the match at the start and end of the string, respectively. The `[a-zA-Z0-9]+` matches one or more alphanumeric characters. The `(\.[a-zA-Z0-9]+){2}` part requires two periods followed by one or more alphanumeric characters for each segment (x, y, and z). If the match is successful, it returns True; otherwise, it returns False.