from DAO.Factory.ConexionFactory import ConexionFactory

class ConexionManager:
    def __init__(self):
        self.datos = None

    def guardarPersonas(self, nombre, apellido, username, password, condicion):
        with ConexionFactory() as con:
            cursor, conexion = con 
            query = "INSERT INTO personas (nombre, apellido, username, passwor, condicion) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(query, (nombre, apellido, username, password, condicion))
            conexion.commit()
            print("Datos insertados")

    def verificarUsuario(self, user, passw):
        with ConexionFactory() as con:
            cursor, conexion = con 
            query = "SELECT * FROM personas WHERE username = %s AND passwor = %s"
            cursor.execute(query, (user, passw))
            datos = cursor.fetchall()
            return (len(datos) > 0) , datos

    def getPersonas(self):
        with ConexionFactory() as con:
            cursor, conexion = con
            query = "SELECT * FROM personas"
            cursor.execute(query)
            datos = cursor.fetchall()
            return datos
