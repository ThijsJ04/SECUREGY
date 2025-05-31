def match_string(target_string):
       match = re.match(r"^[a-zA-Z0-9]+(\.[a-zA-Z0-9]+){2}$", target_string)
       return bool(match) if match else False