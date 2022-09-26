class Bayes:

    def __init__(self, data):
        self.data = data
        self.categories = {}
        self.resumed_data = {}

    def start(self, apriori = None):
        self.categories = self.get_categories()
        self.resumed_data = self.get_resumed_data()

        self.print_result()

    def calculate_probabilities(self):
        pass
    
    def get_categories(self):
        category = list(self.data.keys())[-1]
        categories = {category: {data: 0 for data in self.data[category]}}

        for data in self.data[category]:
            if data not in categories:
                categories[category][data] += 1
        
        return categories

    def get_resumed_data(self):
        resumed_data = {}
        index = 0

        for (key, value) in self.data.items():
            if key != list(self.data.keys())[-1] and key not in resumed_data.keys():
                resumed_data[key] = {data: {category: 0 for category in self.categories[list(self.categories)[0]].keys()} for data in value}
            
            if key in resumed_data.keys():
                for data in value:
                    category = self.data[list(self.data.keys())[-1]][index]
                    resumed_data[key][data][category] += 1
                    index += 1
                
            index = 0
        
        return resumed_data
    
    def print_result(self):
        print(self.categories)
        print(self.resumed_data)