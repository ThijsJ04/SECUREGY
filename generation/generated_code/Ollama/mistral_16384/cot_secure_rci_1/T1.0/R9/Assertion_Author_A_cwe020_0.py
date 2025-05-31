def match_string(target_string):
      return re.match(r'[a-zA-Z0-9]+(\.[a-zA-Z0-9]+)*', target_string) is not None