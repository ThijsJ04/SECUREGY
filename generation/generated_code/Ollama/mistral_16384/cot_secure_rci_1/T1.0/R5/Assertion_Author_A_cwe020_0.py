def match_string(target_string):
      return re.match(r"^[a-zA-Z]+\.[a-zA-Z]+\.[a-zA-Z]+$", target_string) is not None