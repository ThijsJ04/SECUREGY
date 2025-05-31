 def match_string(target_string):
       return re.match(r'^[a-zA-Z0-9]+(\.[a-zA-Z0-9]+)*$', target_string) is not None

This function uses the regular expression `^[a-zA-Z0-9]+(\.[a-zA-Z0-9]+)*$` to check if the input string matches the format 'x.y.z' (where x, y, z are strings). The `re.match()` function returns a match object if the pattern matches at the beginning of the string, or None otherwise. The function checks whether this returned value is not None to determine whether the string is valid.