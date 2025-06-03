import os


def delete_image(path):
    try:
        # Check if the file exists
        if os.path.exists(path):
            # Delete the file
            os.remove(path)
            print("The file has been deleted")
        else:
            print("The file does not exist")
    except Exception as e:
        print("An error occurred: ", str(e))
