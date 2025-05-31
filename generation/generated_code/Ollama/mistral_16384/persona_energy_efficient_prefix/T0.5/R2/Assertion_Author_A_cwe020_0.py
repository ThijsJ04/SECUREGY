 def match_string(target_string):
       return re.match(r'^[a-zA-Z0-9]+(\.[a-zA-Z0-9]+){2}$', target_string) is not None

This function uses the `re` module to check if the input string matches the pattern 'x.y.z'. The regular expression `^[a-zA-Z0-9]+(\.[a-zA-Z0-9]+){2}$` ensures that each part (x, y, z) consists of alphanumeric characters and there are exactly three parts separated by dots.