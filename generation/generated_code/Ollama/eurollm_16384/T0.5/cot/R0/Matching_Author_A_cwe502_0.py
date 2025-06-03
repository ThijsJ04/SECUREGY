import marshal

data = {"key": "value", "another_key": 123}
with open("data.bin", "wb") as f:
    f.write(marshal.dumps(data))
