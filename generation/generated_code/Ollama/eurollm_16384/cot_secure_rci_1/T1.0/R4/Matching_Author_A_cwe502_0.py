from flask import request
import marshal  # Assuming correct import now for demonstration purposes

@app.route('/unmarshal')
def unmarshal_data():
    data = request.get_json() if request.method == 'POST' else {}
    return data