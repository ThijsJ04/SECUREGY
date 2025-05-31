def match_string(target_string):
       return bool(re.match(r'^[a-zA-Z0-9]+(\.[a-zA-Z0-9]+){2}$', target_string))