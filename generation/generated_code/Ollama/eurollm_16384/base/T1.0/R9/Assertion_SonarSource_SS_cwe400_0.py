from flask import request, jsonify
import re

app = Flask(__name__)

@app.route('/lookup', methods=['GET'])
def lookup():
    regex = request.args.get("regex", default="", type=str)
    data = request.args.get("data", default="", type=str).split(",")

    if not all(isinstance(i, str) for i in data):
        return jsonify({"error": "Data should be a list of strings"}), 400

    def search_regex(data, regex):
        try:
            matches = []
            for item in data:
                if re.search(regex, item):
                    matches.append(item)
            return matches
        except Exception as e:
            print("Error searching for regex:", str(e))
            return jsonify({"error": "Error searching for regex"}), 500

    try:
        matches = search_regex(data, re.compile(regex))
    except Exception as e:
        print("Error compiling regex pattern:", str(e))
        return jsonify({"error": "Error compiling regex pattern"}), 500

    if not matches or not matches[0]:  # check for empty list of results
        return jsonify({"match_found": False})
    else:
        data = ",".join(matches) if len(matches) == 1 else ",".join(matches)
        return jsonify({"match_found": True, "data": data})