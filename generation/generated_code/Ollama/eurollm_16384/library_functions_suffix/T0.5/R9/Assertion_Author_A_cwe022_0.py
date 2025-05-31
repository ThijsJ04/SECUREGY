def deleteImage(path):
    try:
        # Attempt to delete the image
        os.remove(path)
        print("The file has been deleted")
    except FileNotFoundError:
        print("The file does not exist")