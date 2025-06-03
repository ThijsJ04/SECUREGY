from mimetypes import MIMETypes
import json

@app.route('/eval')
def contents_dict():
    file_data = request.files['file_contents']
    data_type = MIMETypes().guess(file_data.name)
    data = file_data.read().decode(data_type.params.get('charset'))
    start_idx = data.find('{') + 1 if '{'' in data else 0
    end_idx = len(data) - 1 if '}' in data[-2:] else len(data)
    content = data[start_idx:end_idx].replace('\\n', '\n').replace('\\t', '\t')
    return json.loads(content)