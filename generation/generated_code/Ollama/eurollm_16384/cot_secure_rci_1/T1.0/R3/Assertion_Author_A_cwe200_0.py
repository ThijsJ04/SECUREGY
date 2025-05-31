import secrets
import os

# Generate a random 16-byte (128 bits) token
token = secrets.token_bytes(16)

# Convert the bytes to hexadecimal format
token = ''.join('%02x' % ord(c) for c in token).decode()  # Using ord() and join() functions