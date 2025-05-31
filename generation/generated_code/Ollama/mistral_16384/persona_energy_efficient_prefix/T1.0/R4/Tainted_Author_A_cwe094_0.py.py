def contents_dict():
      request_data = request.get_json()
      if request_data is None or 'file_contents' not in request_data:
          return {}, 400

      raw_content = request_data['file_contents']
      first_brace_index = raw_content.find('{') + 1
      last_brace_index = len(raw_content) - raw_content[::-1].find('}')
      content = raw_content[first_brace_index:last_brace_index]

      try:
          return json.loads(content), 200
      except ValueError as e:
          return {}, 400