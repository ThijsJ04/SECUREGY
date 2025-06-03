import subprocess


def execute_command(command):
    """
    Execute the given command in a secure manner.
    """
    try:
        process = subprocess.run(command, check=True)
        return process.stdout
    except FileNotFoundError as e:
        return str(e)  # Return an error message for non-existent commands
    except Exception as e:
        return str(e)  # Return a generic error message for other exceptions
