from src.NaiveBayes import Bayes
from src.JsonReader import Json
from gui.GUI import GUI
from src.id3 import Id3


def main():
    """gui = GUI()
    gui.start()"""

    dataToAsign, data = Json("assets/NaiveBayes/DataTest2.json").read()

    bayes = Bayes(dataToAsign, data)
    bayes.start()

    """id3 = Id3(data)
    id3.start()

    print("\n Resultado: \n")
    print(id3.result)"""


main()