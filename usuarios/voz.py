import pyttsx3


class Voz:
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[2].id)
    engine.say('Bienvenido al Asistente Viky ')

def AccionesDispobles(sef):
    
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[2].id)
    engine.say("""
    Acciones disponibles:
    - registro.
    - Entrar.
    """)
    engine.runAndWait()

def elegir(sef):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[2].id)  
    engine.say("¿Que quieres hacer? : ")
    engine.runAndWait()  

def secRegistrar(sef):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[2].id)
    engine.say("""
            Okey!! Vamos a registrarte en el Asistente
            """)
    engine.runAndWait()

def secEntrar(sef):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[2].id)
    engine.say("""
            vale!! identificate con tus credenciales
            """)
    engine.runAndWait()    

def recordName(self):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[2].id)
    engine.say('¿Cual es tu nombre?: ')
    engine.runAndWait()
def recordLastname(self): 
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[2].id)   
    engine.say('¿Cual es tu apellido?: ')
    engine.runAndWait()
def recordMail(self): 
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[2].id)   
    engine.say('Ingresa un correo electronico: ')
    engine.runAndWait()
def recordPasswd(self):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[2].id)       
    engine.say('Ingresa una contraseña: ')
    engine.runAndWait()

######################################


def login(self):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[2].id)


def loginMail(self):  
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[2].id)
    engine.say('Ingresa tu correo electronico: ')
    engine.runAndWait()

def loginPass(self):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[2].id)
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[2].id)
    engine.say('Ingresa tu Contraseña: ')
    engine.runAndWait()

recordName(self='*')

recordLastname(self='*')

recordMail(self='*')

recordPasswd(self='*')

login(self='*')

loginMail(self='*')

loginPass(self='*')