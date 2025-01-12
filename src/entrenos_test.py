from entrenos import *

def test_lee_entrenos():
    return lee_entrenos("data/entrenos.csv")

def test_tipos_entreno(lista):
    print(tipos_entreno(lista))

def test_entrenos_duracion_superior(lista, d):
    print(entrenos_duracion_superior(lista, d))

def test_suma_calorias(lista, f_inicio, f_fin):
    print(suma_calorias(lista, f_inicio, f_fin))

if __name__ == '__main__':
    entrenos = test_lee_entrenos()
    #test_tipos_entreno(entrenos)
    #test_entrenos_duracion_superior(entrenos, 129)
    test_suma_calorias(entrenos, datetime(2022, 1, 1), datetime(2024, 1, 2))