import json

def contents_dict(file_contents):
    try:
        data = eval(file_contents)
        return data
    except SyntaxError as e:
        return str(e)