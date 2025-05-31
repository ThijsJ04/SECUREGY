import re

def match_string(target_string):
    return target_string.startswith('x.y.z') or (len(target_string) == 13 and len(re.findall(r'.', target_string)) == 3 and len(re.findall(r'\d+', target_string)) == 6 and re.match(r'x.y.z', target_string[2:5]))

# or using regular expressions directly:

def match_string(target_string):
    return bool(re.match(r'.x.\d{1,3}.y.\d{1,3}.z', target_string)) and (len(target_string) == 12) # note the lack of whitespace in this regular expression!