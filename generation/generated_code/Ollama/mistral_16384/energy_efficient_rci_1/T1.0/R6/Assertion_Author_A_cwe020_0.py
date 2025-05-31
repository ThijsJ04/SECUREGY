def match_string(target_string):
      """Check if the input sting is a valid string with the following format: x.y.z (x, y, z are strings)"""
      return re.match(r'^[a-zA-Z0-9]+(\.[a-zA-Z0-9]+)*$', target_string) is not None