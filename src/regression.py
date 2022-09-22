class Regression:

    def __init__(self, xData, yData):
        self.xData = xData
        self.yData = yData
        self.slope = 0
        self.intercept = 0
        self.x = 0
        self.y = 0
        self.xy = 0
        self.x2 = 0
    
    def start(self):
        self.calculateData()
        self.calculateSlope()
        self.calculateIntercept()

    def calculateData(self):
        self.x = sum(self.xData)
        self.y = sum(self.yData)
        self.xy = sum([self.xData[i] * self.yData[i] for i in range(len(self.xData))])
        self.x2 = sum([self.xData[i] * self.xData[i] for i in range(len(self.xData))])

    def calculateSlope(self):
        n = len(self.xData)
        self.slope = (n * self.xy - self.x * self.y) / (n * self.x2 - self.x * self.x)

    def calculateIntercept(self):
        n = len(self.xData)
        self.intercept = (self.y * self.x2 - self.x * self.xy) / (n * self.x2 - self.x * self.x)

    def predict(self, dataToPredict):
        return self.slope * dataToPredict + self.intercept

    def predictList(self, dataToPredict):
        return [self.slope * data + self.intercept for data in dataToPredict]
