from flask import Flask, request
from mimetypes import MimeTypes
import ast, io
import re

app = Flask(__name__)


@app.route("/eval")
def contents_dict():
    file_contents = request.files["file_contents"].read().decode("utf-8")
    mimetype, _ = MimeTypes().guess(file_contents)
    if mimetype != "application/json":
        return "Invalid data type", 400

    # Remove anything before the first '{' and after the last '}'
    file_contents = re.sub(r"^{|}$", "", file_contents, flags=re.MULTILINE)

    # Evaluate the string as a dictionary
    io_string = io.StringIO(file_contents)
    node = ast.parse(io_string.read(), filename="<string>", mode="exec")
    with ast.Builder(node.body) as builder:
        for stmt in ast.walk(node):
            if isinstance(stmt, (ast.Assign, ast.Dict)):
                exec(compiler.compile(stmt, "<string>", "exec"), builder.glob)
    return builder.asdict()
