import mysql.connector

class ConexionFactory:
    def __init__(self):
        self.host = "localhost"
        self.user = "root"
        self.password = ""
        self.database = "encuestasalud"
        self.cnx = None
        self.cursor=None

    def __enter__(self):
        self.cnx = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor = self.cnx.cursor()
        return self.cursor, self.cnx

    def __exit__(self, exc_type, exc_value, traceback):
        if self.cursor:
            self.cursor.close()
        if self.cnx:
            self.cnx.close()