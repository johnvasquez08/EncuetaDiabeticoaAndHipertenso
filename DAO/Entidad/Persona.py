from DAO.Factory.ConexionManager import ConexionManager

class Persona:
    def __init__(self, nombre, apellido, username, password, condicion):
        self.conexionManager = ConexionManager()
        self.nombre = nombre
        self.apellido = apellido
        self.username = username
        self.password = password
        self.condicion = condicion
    
        
    def save(self):
        self.conexionManager.guardarPersonas(self.nombre, self.apellido, self.username, self.password, self.condicion)
    
    def iniciarSesion(self):
        return self.conexionManager.verificarUsuario(self.username, self.password)
