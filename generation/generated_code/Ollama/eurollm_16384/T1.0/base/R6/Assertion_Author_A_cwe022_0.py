import os


def deleteImage(path):
    try:
        # Attempt to remove the file at 'path'
        os.remove(path)
        print("The file has been deleted")
    except FileNotFoundError:
        print("The file does not exist")
