def contents_dict():
      content = request.files['file_contents'].read().decode('utf-8')
      start_index = content.find('{') + 1
      end_index = content.rfind('}')
      data = eval(content[start_index:end_index])
      return data