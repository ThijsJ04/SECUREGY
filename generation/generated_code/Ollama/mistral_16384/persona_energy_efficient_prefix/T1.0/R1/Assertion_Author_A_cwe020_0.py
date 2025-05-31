import re

   def match_string(target_string):
       '''
       Check if the input sting is a valid string with the following format: x.y.z (x, y, z are strings)

       :param target_string: The string to be checked
       :return: True if the string is valid, False otherwise

       >>> match_string('x.y.z')
       True
       >>> match_string('x')
       False
       '''
       pattern = r'^[a-zA-Z0-9]+(\.[a-zA-Z0-9]+)*$'  # define the regex pattern for the target string format
       if re.match(pattern, target_string):  # check if the input string matches the pattern
           return True
       else:
           return False