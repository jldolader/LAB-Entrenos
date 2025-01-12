from collections import namedtuple
from datetime import datetime
from typing import List

Entreno = namedtuple('Entreno', 'tipo, fechahora, ubicacion, duracion, calorias, distancia, frecuencia, compartido')

def lee_entrenos(ruta: str) -> List[Entreno]:
    with open(ruta, 'r', encoding='utf-8') as f:
        next(f)
        return [Entreno(
                tipo = str(e[0]),
                fechahora = datetime.strptime(e[1], "%d/%m/%Y %H:%M"),
                ubicacion = str(e[2]),
                duracion = int(e[3]),
                calorias = int(e[4]),
                distancia = float(e[5]),
                frecuencia = int(e[6]),
                compartido = bool(True if e[7] == 'S' else False)
            )
            for e in (l.split(',') for l in f)
        ]

def tipos_entreno(lista: List[Entreno]) -> List[str]:
    return sorted(set(l.tipo for l in lista))

def entrenos_duracion_superior(lista: List[Entreno], d: int) -> List[Entreno]:
    return [l for l in lista if l.duracion > d]

def suma_calorias(lista: List[Entreno], f_inicio: datetime, f_fin: datetime) -> int:
    return sum(l.calorias for l in lista if f_inicio <= l.fechahora <= f_fin)