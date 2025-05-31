def match_string(target_string):
      return re.match(r'\w+\.\w+\.\w+', target_string) is not None