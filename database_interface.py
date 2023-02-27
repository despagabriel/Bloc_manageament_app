import json
class Databases():
    def __init__(self, path):
        self.path = path

    def read_data(self):
        '''
        This method can read database
        :return: dictionary
        '''
        with open(self.path, 'r') as file:
            data = json.load(file)
        return data

    def save_data(self, new_data):
        '''
        this method can save the new information in databases
        :param new_data: database
        :return: none
        '''
        with open(self.path, "w") as file:
            json.dump(new_data, file, indent=3)




