from dataclasses import dataclass, field



@dataclass
class Persona:
    nombre: str
    dni: str


@dataclass
class Estudiante:
    ru: str      # ru: registo universitario


@dataclass
class Docente:
    sueldo: float     #float porque tiene pesos
    tirular: bool     #  si tiene titulo o no


@dataclass
class Auxiliar(Estudiante):
    sueldo: int
    nro_item: int


@dataclass
class Paralelo:
    sigla: str
    docente: Docente     # va ser de tipo Docente, de la clase docente
    auxiliar: Auxiliar | None = None      #le puedo enviar un auxiliar | o no.
    estudiantes: list[Estudiante] = field(default_factory=list)          #lista de objetos de estudiantes
    notas: list[int] = field(default_factory=list)  # lista de enteros


@dataclass
class Materia:
    nombre: str
    sigla: str
    paralelos: list[Paralelo] = field(default_factory=list)