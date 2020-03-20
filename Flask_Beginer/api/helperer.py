import json
import os.path

class Converter():
    
    def __init__(self, path):
        self.filename = os.path.join(path)


    def serialization(self, data):
        """
            Method of Serialization.
        """

        with open(self.filename, 'w') as file:
            json.dump(data, file)


    def deserialization(self):
        """
            Method of Deserialization
        """
        with open(self.filename, 'r') as file:
            read_data = json.load(file)
        return read_data