class Autor:
    def __init__(self, nom, pseudo):
        self.__nombre = nom
        self.__pseudonimo = pseudo

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nom):
        self.__nombre = nom

    @property
    def pseudonimo(self):
        return self.__pseudonimo

    @pseudonimo.setter
    def pseudonimo(self, pseudo):
        self.__pseudonimo = pseudo

    def __str__(self):
        return f'Nombre: {self.__nombre}  pseudonimo: {self.__pseudonimo}'

    def escribir(self):
        print(f'{self.__pseudonimo} esta escribiendo su siguiente libro...')


class Libro:
    def __init__(self, tit, aut, an, edit):
        self.__titulo = tit
        self.__autor = aut
        self.__ano = an
        self.__editorial = edit

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, tit):
        self.__titulo = tit

    @property
    def ano(self):
        return self.__ano

    @ano.setter
    def ano(self, an):
        self.__ano = an

    @property
    def editorial(self):
        return self.__editorial

    @editorial.setter
    def editorial(self, edit):
        self.__editorial = edit

    def __str__(self):
        return f'''
            Titulo: {self.__titulo}
            Autor: {self.__autor}
            Ano: {self.__ano}
            Editorial: {self.__editorial}'''

    @classmethod
    def libro_planeta(cls, titulo, autor, ano):
        return cls(titulo, autor, ano, 'planeta')

    def leer(self, minutos):
        print(f'Leyendo por {minutos} minutos')


class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nom):
        self.__nombre = nom

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, ed):
        self.__edad = ed

class Alumno(Persona):
    def __init__(self, nombre, edad, numer_cuenta, carrera, promedio):
        super().__init__(nombre, edad)
        self.__numer_cuenta = numer_cuenta
        self.__carrera = carrera
        self.__promedio = promedio

