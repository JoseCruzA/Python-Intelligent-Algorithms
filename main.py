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



    """bayes = Bayes(data)
    bayes.start()"""

    """id3 = Id3(data)
    id3.start()

    print("\n Resultado: \n")
    print(id3.result)"""


main()