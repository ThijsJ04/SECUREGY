 def match_string(target_string):
       return re.match(r'^[a-zA-Z0-9]+(\.[a-zA-Z0-9]+)*$', target_string) is not None

This function uses a regular expression to check if the input string follows the format x.y.z, where each part (x, y, z) consists of alphanumeric characters only. If the match is successful, it returns True; otherwise, it returns False.