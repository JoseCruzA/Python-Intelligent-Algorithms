from src.NaiveBayes import Bayes
from src.JsonReader import Json
from gui.GUI import GUI
from src.id3 import Id3
from src.KNN import Knn


def main():
    """gui = GUI()
    gui.start()"""

    dataToAsign, data, k = Json("assets/KNN/DataTest1.json").read()

    """bayes = Bayes(dataToAsign, data)
    bayes.start()"""

    """data = Json("assets/id3/DataTest1.json").read()

    id3 = Id3(data)
    id3.start()"""

    knn = Knn(data, dataToAsign, k)
    knn.start()


main()