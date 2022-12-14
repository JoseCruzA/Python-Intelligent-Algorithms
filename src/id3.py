from calendar import c
from unicodedata import category
from math import log2
from numpy import abs


class Id3:

    def __init__(self, data):
        self.data = data
        self.categories = {}
        self.resumed_data = {}
        self.entropies = {}
        self.result = {}
    
    def start(self):
        self.categories = self.get_categories()
        self.resumed_data = self.get_resumed_data()
        self.entropies = self.get_entropies()
        self.result = self.get_result()

        self.print_result()

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
    
    def get_entropies(self):
        entropies = {data: 0 for data in self.resumed_data.keys()}

        for (key, value) in self.resumed_data.items():
            entropies[key] = self.get_entropy(value)
        
        return dict(sorted(entropies.items(), key=lambda x: x[1]))

    def get_entropy(self, data):
        entropy = 0

        for (key, value) in sorted(data.items()):
            entropy += (sum(value.values()) / (len(self.data) + 1)) * self.get_entropy_value(value)
        
        return entropy

    def get_entropy_value(self, data):
        entropy_value = 0

        for value in data.values():
            if value != 0:
                entropy_value += -(value / sum(data.values())) * log2(value / sum(data.values()))
        
        return entropy_value

    def get_result(self):
        current_category = list(self.entropies.keys())[0]
        result = {current_category: {}}

        for (key, value) in self.resumed_data[current_category].items():
            for (category, count) in value.items():
                if count == sum(value.values()):
                    result[current_category][key] = category
                    break
        
        for (key, value) in self.resumed_data[current_category].items():
            for (category, count) in value.items():
                if count != sum(value.values()) and key not in result[current_category].keys():
                    result[current_category][key] = self.update_data(current_category, result[current_category].keys())
                    break
        
        return result

            

    def update_data(self, current_category, data_to_remove):
        index_to_remove = []
        data = {}

        for i in range(len(self.data[current_category])):
            if self.data[current_category][i] in data_to_remove:
                index_to_remove.append(i)

        for (key, value) in self.data.items():
            if key != current_category:
                data[key] = [value[i] for i in range(len(value)) if i not in index_to_remove]
        
        id3 = Id3(data)
        id3.start()
        
        return id3.get_result()

    def print_result(self):
        print(self.categories)
        print(self.resumed_data)
        print(self.entropies)
        print("\n")