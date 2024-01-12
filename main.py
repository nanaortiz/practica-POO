"""
IMPORTANTE:
Al crear la clase Estudiante, agregar la siguiente función

def __hash__(self):
    return int(sha256(self.ru.encode()).hexdigest(), 16)

Esta permitirá que pueda ser utilizado en un diccionario
"""


from random import random
import pickle
from clases import *   # ese asteristo significa importar todo
from collections import defaultdict


def adicionar_materia_a_archivo(materia, filename="materias.dat"):
    #para abrir un archivo y escribir en el 
    with open(filename, "a+b") as f:
        #sintaxis para escribir un objeto a un archivo  usando pickle
        pickle.dump(materia, f)


def estudiante_en_dos_materias(filename="materias.dat"):
    repetidos = defaultdict(int)
    pass

# creacion de objetos
def main():
    estudiantes = [
        Estudiante(nombre=f"E{i}", dni=f"{i}" * 3, ru=f"{i}" * 4) for i in range(1, 7)
    ]

    docentes = [
        Docente(
            nombre=f"D{i}", dni=f"{i}", sueldo=round(random() * 10000, 2), titular=True
        )
        for i in range(8, 11)
    ]

    paralelo_1 = Paralelo(
        sigla="p1", docente=docentes[0], estudiantes=estudiantes[:2], notas=[50, 20]
    )
    paralelo_2 = Paralelo(
        sigla="p2", docente=docentes[1], estudiantes=estudiantes[2:4], notas=[60, 100]
    )
    paralelo_3 = Paralelo(
        sigla="p3",
        docente=docentes[2],
        estudiantes=estudiantes[4:] + [estudiantes[0]],
        notas=[40, 30, 10],
    )

    m1 = Materia(nombre="M1", sigla="M1", paralelos=[paralelo_1, paralelo_2])
    m2 = Materia(nombre="M2", sigla="M2", paralelos=[paralelo_3])

    print(m1)
    print(m2)
    # Adicionar todas las materias al archivo

    # Mostrar los estudiantes que están en en ambas materias


if __name__ == "__main__":
    main()