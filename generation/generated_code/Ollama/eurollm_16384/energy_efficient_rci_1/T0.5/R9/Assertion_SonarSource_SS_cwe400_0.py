from flask import request, jsonify
import re

app = Flask(__name__)

@app.route('/lookup', methods=['GET'])
def lookup():
    """
    Search for a regex pattern in the provided data.
    If found, return "Match found", otherwise return "No match found".
    """
    try:
        # Get regex and data from request
        data = request.json
        regex = re.compile(data['pattern'])  # Assuming 'pattern' is in JSON data
        matches = [m for m in regex.finditer(data['text'])]

        if matches:
            return jsonify({"result": "Match found"})
        else:
            return jsonify({"result": "No match found"})
    except KeyError as e:
        print(f"Missing key: {e}")
        return jsonify({"error": f"Missing key: {e}"}), 400
    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({"error": "Internal Server Error"}), 500

if __name__ == '__main__':
    app.run(debug=True)