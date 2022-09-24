from gui.GUI import GUI
from src.id3 import Id3


def main():
    """gui = GUI()
    gui.start()"""

    data = {
        "Antenas": [1, 1, 1, 0, 1, 2],
        "Colas": [0, 0, 2, 2, 1, 2],
        "Nucleos": [2, 1, 0, 1, 1, 1],
        "Cuerpo": ["Rayado", "Blanco", "Rayado", "Rayado", "Rayado", "Rayado"],
        "Clase": ["Normal", "Cancerigena", "Normal", "Normal", "Cancerigena", "Cancerigena"]
    }


    id3 = Id3(data)
    id3.start()

    print("\n Resultado: \n")
    print(id3.result)


main()