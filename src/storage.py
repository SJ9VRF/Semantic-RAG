# Class for handling data storage
import json
import os

class StorageManager:
    def __init__(self, config):
        self.config = config
        self.data_dir = "data_storage"  # Directory to store data files
        os.makedirs(self.data_dir, exist_ok=True)

    def save(self, data, key):
        """
        Saves data to a JSON file. Each set of data is associated with a unique key.
        """
        file_path = os.path.join(self.data_dir, f"{key}.json")
        with open(file_path, 'w') as file:
            json.dump(data, file)
        print(f"Data saved under key {key} at {file_path}")

    def load(self, key):
        """
        Loads data from a JSON file based on the provided key.
        """
        file_path = os.path.join(self.data_dir, f"{key}.json")
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                data = json.load(file)
            print(f"Data loaded for key {key}")
            return data
        else:
            print(f"No data found for key {key}")
            return None
