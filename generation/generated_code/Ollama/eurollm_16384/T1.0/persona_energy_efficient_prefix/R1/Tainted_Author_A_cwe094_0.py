from flask import Flask, request

app = Flask(__name__)


@app.route("/eval", methods=["POST"])
def contents_dict():
    data = request.get_json()  # Assuming JSON format
    if "file_contents" in data:
        content = data.pop("file_contents")
        return {
            k: v
            for k, v in (
                {
                    key: value[1:-1] if isinstance(value, str) else eval(str(value))
                    for key, value in content.items()
                }.items()
            )
            if not (
                isinstance(v, dict)
                and any("eval" in k or "__name__" in k or "__qualname__" in k)
                and isinstance(v, str)
            )
        }
    else:
        return "No file_contents provided."
