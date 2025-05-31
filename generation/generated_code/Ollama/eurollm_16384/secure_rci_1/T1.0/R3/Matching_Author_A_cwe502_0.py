import marshal
from flask import Flask, request

app = Flask(__name__)

@app.route('/unmarshal', methods=['GET'])
def unmarshal_data():
    data = request.args.get('data')  # Retrieve the marshalled data from the GET query string

    if data:
        # Unmarshal the data by converting it from hex to bytes
        try:
            unmarshalled_data = marshal.loads(data, encoding='utf-8')  # Marshal loads takes bytes as input
            return unmarshalled_data
        except Exception as e:
            print(f"Error unmarshalling data: {e}")
    else:
        print("No data provided in the GET query string.")