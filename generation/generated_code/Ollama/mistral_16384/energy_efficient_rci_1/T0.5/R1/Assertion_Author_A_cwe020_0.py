def match_string(target_string):
       if re.match(r'[a-zA-Z0-9]+(?:\.[a-zA-Z0-9]+){2}', target_string):
           return True
       else:
           return False