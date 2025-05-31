 def match_string(target_string):
        if not target_string or not re.match(r'^[a-zA-Z0-9]+(\.[a-zA-Z0-9]+)*$', target_string):
            return False
        parts = target_string.split('.')
        return all([part for part in parts if part])

This implementation checks if the input string is non-empty, matches the specified pattern (x.y.z where x, y, z are strings), and each part of the string is not empty. If all conditions are met, it returns True; otherwise, False.