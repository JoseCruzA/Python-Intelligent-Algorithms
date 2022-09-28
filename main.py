from src.FPGrowth import FPGrowth
from src.NaiveBayes import Bayes
from src.JsonReader import Json

from src.id3 import Id3
from src.KNN import Knn


def main():
    """gui = GUI()
    gui.start()"""

    """data = Json("assets/id3/DataTest1.json").read()

    id3 = Id3(data)
    id3.start()"""

    #dataToAsign, data = Json("assets/NaiveBayes/DataTest3.json").read()

    """bayes = Bayes(dataToAsign, data)
    bayes.start()"""

    """dataToAsign, data, k = Json("assets/KNN/DataTest2.json").read()

    knn = Knn(data, dataToAsign, k)
    knn.start()"""


    data = Json("assets/FPGrowth/DataTest.json").read()

    Fp = FPGrowth(data)
    Fp.start()

main()


"""from src.APRIORI import APRIORI
from src.JSONReader import JSONReader

def main():
    data = JSONReader("assets\Test.json").reader()
    Apriori = APRIORI(data)
    Apriori.start(0.60, 0.3334)

main()"""