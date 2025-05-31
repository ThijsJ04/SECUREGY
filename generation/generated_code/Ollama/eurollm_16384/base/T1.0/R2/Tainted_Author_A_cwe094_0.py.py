from flask import Flask, request, jsonify
import yaml

app = Flask(__name__)

@app.route('/eval', methods=['POST'])
def eval_yaml():
    data = {"file_contents": request.form["file_contents"]} 
    with open('data.yaml', 'r') as yamlfile:
        config = yaml.safe_load(yamlfile)  # Read the YAML configuration file.
    config['file_contents'] = data['file_contents'] # Update the file contents in the configuration.
    with open('data.yaml', 'w') as outfile: 
        yaml.dump(config, outfile)  # Write the updated YAML to a new file.
    return jsonify(data['file_contents']) # Return the updated file contents as JSON.