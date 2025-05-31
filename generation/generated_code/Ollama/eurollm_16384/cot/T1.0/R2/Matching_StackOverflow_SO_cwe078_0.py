def execute_bash():
    try:
        # ... your current code here ... 
    except subprocess.CalledProcessError as e:  # or other exception types, depending on what might go wrong
        print(f"Error executing command: {e}")
        return "Command not recognized"