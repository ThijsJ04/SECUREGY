def match_string(target_string):
       pattern = r"^[a-zA-Z]+\.[a-zA-Z]+\.[a-zA-Z]+$"
       return re.match(pattern, target_string) is not None