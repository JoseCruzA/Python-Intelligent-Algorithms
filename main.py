from gui.GUI import GUI
from src.id3 import Id3


def main():
    """gui = GUI()
    gui.start()"""

    """data = {
        "Antenas": [1, 1, 1, 0, 1, 2],
        "Colas": [0, 0, 2, 2, 1, 2],
        "Nucleos": [2, 1, 0, 1, 1, 1],
        "Cuerpo": ["Rayado", "Blanco", "Rayado", "Rayado", "Rayado", "Rayado"],
        "Clase": ["Normal", "Cancerigena", "Normal", "Normal", "Cancerigena", "Cancerigena"]
    }"""

    data = {
        "Pronóstico": ["Soleado", "Soleado", "Nublado", "Lluvia", "Lluvia", "Lluvia", "Nublado", "Soleado", "Soleado", "Lluvia", "Soleado", "Nublado", "Nublado", "Soleado"],
        "Temperatura": ["Alta", "Alta", "Alta", "Moderada", "Baja", "Baja", "Baja", "Moderada", "Baja", "Moderada", "Moderada", "Moderada", "Alta", "Moderada"],
        "Humedad": ["Alta", "Alta", "Alta", "Alta", "Normal", "Normal", "Normal", "Alta", "Normal", "Normal", "Normal", "Alta", "Normal", "Alta"],
        "Viento": ["Flojo", "Fuerte", "Flojo", "Flojo", "Flojo", "Fuerte", "Fuerte", "Flojo", "Flojo", "Flojo", "Fuerte", "Fuerte", "Flojo", "Fuerte"],
        "¿Adecuado?": ["No", "No", "Si", "Si", "Si", "No", "Si", "No", "Si", "Si", "Si", "Si", "Si", "No"]
    }

    id3 = Id3(data)
    id3.start()

    print("\n Resultado: \n")
    print(id3.result)


main()