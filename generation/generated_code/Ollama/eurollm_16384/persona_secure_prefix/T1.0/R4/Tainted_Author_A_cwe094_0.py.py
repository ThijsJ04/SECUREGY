from flask import Flask, request
import json 

app = Flask(__name__)

@app.route('/eval', methods=['POST'])
def contents_dict():
    data = request.get_json()
    return json.dumps({
        "result": eval("{" + data["file_contents"] + "}")
    }) 

if __name__ == '__main__':
    app.run(debug=True)