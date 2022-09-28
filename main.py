from src.FPGrowth import FPGrowth
from src.APRIORI import APRIORI
from src.NaiveBayes import Bayes
from src.JsonReader import Json
from src.K_means import K_means
import random
from gui.GUI import GUI
from src.id3 import Id3
from src.KNN import Knn


def main():
    """gui = GUI()
    gui.start()"""

    """data = Json("assets/kmeans/DataTest1.json").read()

    rand=random.sample(range(2, len(data)), 1)
    rand.append(1)
    print(rand)
    Kmeans= K_means(data,2,rand)
    Kmeans.start()"""


    """dataToAsign, data = Json("assets/NaiveBayes/DataTest2.json").read()"""
    """data = Json("assets/id3/DataTest1.json").read()

    id3 = Id3(data)
    id3.start()"""

    """dataToAsign, data = Json("assets/NaiveBayes/DataTest3.json").read()

    bayes = Bayes(dataToAsign, data)
    bayes.start()"""

    """dataToAsign, data, k = Json("assets/KNN/DataTest2.json").read()

    knn = Knn(data, dataToAsign, k)
    knn.start()"""

    """data = Json("assets/FPGrowth/DataTest.json").read()

    Fp = FPGrowth(data)
    Fp.start()"""

    """data = Json("assets\APRIORI\Test.json").read()

    Apriori = APRIORI(data)
    Apriori.start(0.60, 0.3334)"""


main()
