import secrets

# Generate a 16-byte (128-bit) random number suitable for managing passwords/secrets
secret_key = secrets.token_bytes(16)
print(secret_key)  # Output: bytes object containing 16 random bytes