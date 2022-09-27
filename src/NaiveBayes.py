from src.Algorithm import Algorithm


class Bayes(Algorithm):

    def __init__(self, dataToAsign, data):
        Algorithm.__init__(self, data)
        self.dataToAsign = dataToAsign
        self.resumed_data = {}
        self.probabilities = {}
        self.result = {}

    def start(self, apriori = 1):
        self.categories = self.get_categories()
        self.resumed_data = self.get_resumed_data()
        self.probabilities = self.calculate_probabilities()
        self.result = self.calify_data(apriori)

        self.print_result(apriori)

    def get_resumed_data(self):
        resumed_data = {
            category: {
                attr: {value: 1 for value in sorted(data)} for (attr, data) in self.data.items() if attr not in self.categories.keys()
            } for category in self.categories[list(self.categories)[0]].keys()
        }
        index = 0
        
        for (key, value) in self.data.items():
            for data in value:
                if key not in self.categories.keys():
                    resumed_data[self.data[list(self.data.keys())[-1]][index]][key][data] += 1
                    index += 1
            
            index = 0

        return resumed_data
    
    def calculate_probabilities(self):
        probabilities = {key: {attr: data for (attr, data) in value.items()} for (key, value) in self.resumed_data.items()}

        for (key, data) in probabilities.items():
            for (attr, value) in data.items():
                probabilities[key][attr] = {key: totalData / sum(data[attr].values()) for (key, totalData) in value.items()}
        
        return probabilities
    
    def calify_data(self, apriori):
        results = {key: 0 for key in self.probabilities.keys()}
        index = 0

        for (key, data) in self.probabilities.items():
            results[key] = (apriori/self.categories[list(self.categories.keys())[0]][key])
            for attr in data.keys():
                results[key] *= (data[attr][self.dataToAsign[index]])
                index += 1
            index = 0
        
        results = dict(sorted(results.items(), key=lambda x: x[1], reverse=True))
        return results

    
    def print_result(self, apriori):
        print("Naive Bayes\n")
        print("Data Clasification:\n {}\n".format(self.categories))
        print("Data Model:\n {}\n".format(self.resumed_data))
        print("Apriori probabilities for class apriori -> {}:\n {}\n".format(apriori, self.probabilities))
        print("For the data {} the probabilities are:\n {}\n".format(self.dataToAsign, self.result))
        print("For the data {} the result is: {}".format(self.dataToAsign ,list(self.result.keys())[0]))