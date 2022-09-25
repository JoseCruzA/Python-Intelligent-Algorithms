import json


class Json:

    def __init__(self, path):
        self.path = path

    def read(self):
        with open(self.path) as file:
            data = json.load(file)

            if "axis_x" in data.keys():
                return (data["axis_x"]["name"], 
                    data["axis_y"]["name"], 
                    data["axis_x"]["data"], 
                    data["axis_y"]["data"], 
                    data["dataToPredict"])
            
            return data