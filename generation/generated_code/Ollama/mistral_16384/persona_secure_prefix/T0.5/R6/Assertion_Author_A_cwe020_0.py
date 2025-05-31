def match_string(target_string):
       pattern = r"[a-zA-Z0-9]+(\.){2}[a-zA-Z0-9]+$"
       return re.match(pattern, target_string) is not None