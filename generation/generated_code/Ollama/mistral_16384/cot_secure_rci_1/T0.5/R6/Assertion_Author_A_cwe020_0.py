 def match_string(target_string):
       return re.match(r'^[a-zA-Z0-9]+(\.[a-zA-Z0-9]+)*$', target_string) is not None

This implementation uses a regular expression to check if the input string matches the desired format (x.y.z, where x, y, z are strings). The regular expression `^[a-zA-Z0-9]+(\.[a-zA-Z0-9]+)*$` means that the string starts with one or more alphanumeric characters (`[a-zA-Z0-9]+`), followed by zero or more groups of a dot and one or more alphanumeric characters (`(\.[a-zA-Z0-9]+)*`). The `^` and `$` symbols ensure that the entire string matches this pattern.