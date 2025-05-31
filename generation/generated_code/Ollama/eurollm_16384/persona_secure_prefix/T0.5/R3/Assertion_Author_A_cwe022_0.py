def deleteImage(path):
    try:
        # Attempt to delete the file at the given path.
        os.remove(path)
        print("The file has been deleted.")
    except FileNotFoundError:
        print("The file does not exist.")