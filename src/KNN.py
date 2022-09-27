from src.Algorithm import Algorithm


class Knn(Algorithm):

    def __init__(self, data, k):
        Algorithm.__init__(self, data)
        self.k = k
        self.resumen_data = {}
    
    
    