import os
from flask import request

def delete_image(path):
    try:
        if os.path.exists(path):
            os.remove(path)
            print("The file has been deleted")
            return "The file has been deleted"
    except Exception as e:
        print("An error occurred: ", str(e))
        return "An error occurred"