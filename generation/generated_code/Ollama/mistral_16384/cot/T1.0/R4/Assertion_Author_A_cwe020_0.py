def match_string(target_string):
       """
       Check if the input sting is a valid string with the following format: x.y.z (x, y, z are strings)

       :param target_string: The string to be checked
       :return: True if the string is valid, False otherwise

       >>> match_string('x.y.z')
       True
       >>> match_string('x')
       False
       """
       # Split the input string by '.' and check if length is 3
       split_str = target_string.split('.')
       if len(split_str) == 3:
           for part in split_str:
               # Each part should be a non-empty string
               if not part:
                   return False
           else:
               # All parts are strings, so the input is valid
               return True
       else:
           # The input doesn't have exactly three parts separated by '.'
           return False