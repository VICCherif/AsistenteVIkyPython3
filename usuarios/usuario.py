import hashlib
import usuarios.db as conexion

connect = conexion.conectar()
database = connect[0]
cursor = connect[1]

class Usuario:

    def __init__(self, nombre, apellidos, email, passwd, fecha):

        self.nombre = nombre

        self.apellidos = apellidos

        self.email = email

        self.passwd = passwd

        self.fecha = fecha

    def registrar(self):

        cifrado = hashlib.sha256()
        cifrado.update(self.passwd.encode('utf8'))

        sql = "INSERT INTO usuarios VALUES(NULL, %s, %s, %s, %s, %s)"

        usuario = (self.nombre, self.apellidos,
                   self.email, cifrado.hexdigest(), self.fecha)

        try:
            cursor.execute(sql, usuario)
            database.commit()
            return[cursor.rowcount, self]
        
        except:
            result = [0, self]

        return result
    def indentificar(self):

        sql = "SELECT * FROM usuarios WHERE email = %s AND passwd = %s"   
        cifrado = hashlib.sha256()
        cifrado.update(self.passwd.encode('utf8')) 
        usuario  = (self.email, cifrado.hexdigest())

        cursor.execute(sql, usuario)
        result = cursor.fetchone()

        return result

