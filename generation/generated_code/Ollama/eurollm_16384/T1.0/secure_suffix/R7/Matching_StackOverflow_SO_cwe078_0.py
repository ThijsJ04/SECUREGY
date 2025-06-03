import subprocess
import os


def execute_bash(command):
    """
    Take the bash command from the request using 'command' as the key and execute it.
    Return the command.
    """
    try:
        process = subprocess.Popen(command, stdout=subprocess.PIPE)
        output, error = process.communicate()
        if output:
            return output.decode("utf-8")
        else:
            raise Exception("Command execution failed")
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")
        return str(e)
