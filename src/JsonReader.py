import json


class Json:

    def __init__(self, path):
        self.path = path

    def read(self, index):
        with open(self.path) as file:
            data = json.load(file)

            return (data[index]["axis_x"]["name"], 
                data[index]["axis_y"]["name"], 
                data[index]["axis_x"]["data"], 
                data[index]["axis_y"]["data"], 
                data[index]["dataToPredict"])