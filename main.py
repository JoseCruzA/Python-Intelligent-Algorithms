from src.NaiveBayes import Bayes
from src.JsonReader import Json
from src.K_means import K_means
import random
from gui.GUI import GUI
from src.id3 import Id3


def main():
    """gui = GUI()
    gui.start()"""

    data = Json("assets/kmeans/DataTest1.json").read()

    rand=random.sample(range(2, len(data)), 1)
    rand.append(1)
    print(rand)
    Kmeans= K_means(data,2,rand)
    Kmeans.start()


    """dataToAsign, data = Json("assets/NaiveBayes/DataTest2.json").read()

    bayes = Bayes(dataToAsign, data)
    bayes.start()"""

    """data = Json("assets/id3/DataTest1.json").read()

    id3 = Id3(data)
    id3.start()"""


main()