This is a good start, but there are a few things you can improve on:

1. Error handling: You should add error handling to make sure that if an error occurs when executing the bash command, your function will handle it gracefully and return something useful instead of crashing.
2. Input validation: Make sure that the input is valid before trying to execute a command. For example, you can check that the value of 'command' is not None or empty string.
3. Security considerations: When executing commands from user input, it's important to be careful and make sure that the commands are safe to run. You might want to consider using a whitelist of allowed commands instead of a blacklist of disallowed commands.