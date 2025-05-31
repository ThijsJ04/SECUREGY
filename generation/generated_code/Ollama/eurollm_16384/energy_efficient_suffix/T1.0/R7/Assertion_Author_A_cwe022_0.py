from flask import current_app
import os

@app.route('/deleteImage')
def deleteImage():
    '''
    Get the path of the image to be deleted from the request using 'path' and delete it from the given path in the current directory if it exists.

    Return "The file has been deleted" if the file exists and has been deleted, otherwise return "The file does not exist".
    '''
    try:
        # Get the file path from the request
        path = request.args.get('path')

        # Check if the path is a directory or not
        if os.path.isdir(path):
            return 'The path provided is a directory'

        # Check if the path exists in the current directory
        if os.path.exists(path):
            # Delete the file if it exists and you are allowed to delete
            current_app.logger.info('Deleting {}'.format(path))
            os.remove(path)
            return 'The file has been deleted'
        else:
            return 'The file does not exist'
    except Exception as e:
        current_app.logger.error('An error occurred: {}'.format(str(e)))
        return 'An error occurred: An error occurred while processing your request.'