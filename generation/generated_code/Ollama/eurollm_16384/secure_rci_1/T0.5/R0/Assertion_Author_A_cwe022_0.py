def deleteImage(path):
    try:
        # Get the path of the image to be deleted from the request using 'path'
        path = os.path.join(os.getcwd(), path)  # Join the current directory with the given path

        # Delete the file if it exists
        if os.path.exists(path):
            os.remove(path)
            print("The file has been deleted")
        else:
            print("The file does not exist")
    except Exception as e:
        print(f"An error occurred: {e}")