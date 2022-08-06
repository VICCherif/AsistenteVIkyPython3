import notas.nota as modelo

class Acciones:
    def crear(self, usuario):
        print(f"Okey !! {usuario[1]} !! Vamos a crear una nueva nota")
        titulo = input("Introduce el titulo de tu nota: ")
        descripcion = input("Dale ingresa tu apuntes")

        nota = modelo.Nota(usuario[0], titulo, descripcion)
        guardar = nota.guardar()

        if guardar[0] >= 1:
            print(f"\nPerfecto has guardado la nota: {nota.titulo}")
        else:
            print(f"\nNo se ha guardado la nota, lo siento {usuario[1]}")

    def mostrar(self, usuario):
        print(f"\nOkey !! {usuario[1]}!! Aquí tienes tus notas: ") 

        nota = modelo.Nota(usuario[0], "", "")   
        notas = nota.listar()

        print(notas)          

