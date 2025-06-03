import cPickle as pickle  # Import 'cPickle' module to marshall data

# Example data to be marshaled
example_data = {"key": "value", "another": [1, 2, 3]}


def marshal_data(data):
    """Marshall the given data."""
    pickled_data = pickle.dumps(data)  # Convert dictionary to bytes using pickling
    return pickled_data
