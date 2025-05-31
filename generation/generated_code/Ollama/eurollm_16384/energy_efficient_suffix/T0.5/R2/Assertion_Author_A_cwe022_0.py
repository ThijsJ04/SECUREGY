import os
from flask import request

def delete_image(path):
    try:
        if os.path.exists(path) and os.path.isfile(path):
            os.remove(path)
            return "The file has been deleted"
        else:
            return "The file does not exist"
    except Exception as e:
        return str(e)