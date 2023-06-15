from cosas import Libro, Autor, Alumno
def main():
    l1 = Libro.libro_planeta("el perfume", Autor("Patrik", "ps"), 1980)
    print(l1)

    print('__________________________herencia------------------')
    al2 = Alumno('Jose', 19, "23232", 'ICO', 9)
    al2.nombre = 'Pepe'
    print(vars(al2))

main()