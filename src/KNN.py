from math import sqrt, pow
from src.Algorithm import Algorithm


class Knn():

    def __init__(self, data, dataToAsign, k):
        self.data = data
        self.k = k
        self.dataToAsign = dataToAsign
        self.resumen_data = {}
        self.distances = {}
        self.near_data = {}
        self.result = None

    def start(self):
        self.resumen_data = self.get_resumen_data()
        self.distances = self.calculate_distances()
        self.near_data = dict(list(self.distances.items())[:self.k])
        self.result = self.clasify_data()
        self.print_result()

    def get_resumen_data(self):
        resumen_data = {(self.data[list(self.data.keys())[0]][i], self.data[list(self.data.keys())[
                         1]][i]): self.data[list(self.data.keys())[2]][i] for i in range(len(self.data[list(self.data.keys())[0]]))}

        return resumen_data

    def calculate_distances(self):
        distances = {key: [value]
                     for (key, value) in self.resumen_data.items()}

        for key in self.resumen_data.keys():
            distance = sqrt(
                pow((self.dataToAsign[0] - key[0]), 2) + pow((self.dataToAsign[1] - key[1]), 2))
            distances[key].append(distance)

        return dict(sorted(distances.items(), key=lambda x: x[1][1]))

    def clasify_data(self):
        near_classes = {value[0]: 0 for value in self.near_data.values()}

        for value in self.near_data.values():
            near_classes[value[0]] += 1

        return max(near_classes, key=near_classes.get)

    def print_result(self):
        print(self.resumen_data)
        print(self.distances)
        print(self.near_data)
        print("For data {} with k = {} the result is: {}".format(
            tuple(self.dataToAsign), self.k, self.result))
