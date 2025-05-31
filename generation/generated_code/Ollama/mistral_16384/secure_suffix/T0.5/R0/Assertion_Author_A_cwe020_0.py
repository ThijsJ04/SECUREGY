def match_string(target_string):
       if re.match(r'[a-zA-Z]+(\.[a-zA-Z]+)*', target_string):
           return True
       else:
           return False