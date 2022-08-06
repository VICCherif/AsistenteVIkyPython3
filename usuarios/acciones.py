import usuarios.usuario as modelo
import notas.acciones
import speech_recognition as sr
import pyttsx3
import datetime
import time


class Acciones:

    r = sr.Recognizer()        
    print("""
    Bienvenidos Al Asistente Viky
    """)
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[2].id)
    engine.say("""
    Bienvenidos Al Asistente Viky
    """)

    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[2].id)
    engine.say("""
    Acciones disponibles:
        -registro.
        -Entrar
    """)
    print("""
    Acciones disponibles:
        -registro.
        -Entrar
    """)
    engine.runAndWait()
    engine.say("¿Que quieres hacer? : ")
    engine.runAndWait()


    def registro(self):
        print("""
        Okey!! Vamos a registrarte en el Asistente
            """)
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[2].id)
        engine.say("""
        Okey!! Vamos a registrarte en el Asistente
        """)
        engine.runAndWait()

        engine.say('¿Cual es tu nombre?: ')
        engine.runAndWait()
        nombre = input('¿Cual es tu nombre?: ')

        engine.say('¿Cual es tu apellido?: ')
        engine.runAndWait()
        apellidos = input('¿Cual es tu apellido?: ')

        engine.say('Ingresa un correo electronico: ')
        engine.runAndWait()
        email = input('Ingresa un correo electronico: ')

        engine.say('Ingresa una contraseña: ')
        engine.runAndWait()
        passwd = input('Ingresa una contraseña: ')

        fecha = datetime.date.today()

        usuario = modelo.Usuario(nombre, apellidos, email, passwd, fecha)

        registro = usuario.registrar()

        if registro[0] >= 1:

            print(
                f"perfecto {registro[1].nombre} te has registrado con el email {registro[1].email}")
            engine.say(f"perfecto {registro[1].nombre} te has registrado con el email {registro[1].email}")
            engine.runAndWait()    

        else:

            print("NO TE HAS REGISTRADO CORRECTAMENTE")

    def login(self):
        
        dia = time.strftime("%d/%m/%y")
        hora = time.strftime("%H:%M:%S")
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[2].id)

        try:
            print("\nIdentificate en el sistema")
            engine.say("Hola,  Identificate en el sistema.")
            engine.runAndWait()

            engine.say("introduce tu correo: ")
            engine.runAndWait()
            email = input("introduce tu correo: ")

            engine.say("ingresa tu contraseña: ")
            engine.runAndWait()
            passwd = input("ingresa tu contraseña: ")

            usuario = modelo.Usuario('', '', email, passwd,'')

            login = usuario.indentificar()


            if email == login[3]:
                print(f"BIenvenido {login[1]} {login[2]}, soy Viky, Hoy es {dia} y la hora es {hora},  ¿En que puedo ayudarte?.")
                engine.say(f"BIenvenido {login[1]} {login[2]}, soy Viky, Hoy es {dia} y la hora es {hora},  ¿En que puedo ayudarte?.")
                engine.runAndWait()
                self.proximasAcciones(login)
        except Exception as e:
            print(type(e))
            print(type(e).__name__)
            print(f"Ingreso Incorrecto, verifica tus datos o intentalo mas tarde")
            engine.say("Ingreso Incorrecto, verifica tus datos ó intentalo mas tarde")
            engine.runAndWait()      

    def proximasAcciones(self, usuario):

        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[2].id)

        print("""
        Tienes Varias Acciones disponibles:
            - Buscar en Google (buscar)
            - Escichar Música (escuchar)
            - Crear Nota (crear)
            - Mostrar nota (mostrar)
            - Eliminar nota (Eliminar)
            - salir
        \n - """)

        engine.say("""
        Tienes Varias Acciones disponibles:
            - Buscar en Google
            - Escuchar Música
            - Crear Nota
            - Mostrar nota 
            - Eliminar nota 
            - salir
        """)
        engine.runAndWait() 


        engine.say("Pues dime que vas a elegir.")
        engine.runAndWait()      
        accion = input("Pues dime que vas a elegir: \n - ")
        hazEl = notas.acciones.Acciones()

        if accion == "buscar":
            print("Vamos al buscador de Google")
            import usuarios.GoogleSeach as google
            google.busqueda()
        elif accion == "escuchar":
            f = open("rocola.pyw", "r")
            print(f.read())
        elif  accion == "crear":
            hazEl.crear(usuario)
            print("Perfecto vamos crear tu nota")
        elif accion == "mostrar":
            hazEl.mostrar(usuario)
        elif accion == "Eliminar": 
            print("Elimar!!")
        elif accion == "salir":      
            print(f"Ok {usuario[1]}, hasta pronto !!!")
            exit()