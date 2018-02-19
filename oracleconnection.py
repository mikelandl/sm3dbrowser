import cx_Oracle

class OracleConnection():

    """Oracle connection class"""

    def __init__(self, username, password, hostname, port, sid):
        self.username = username
        self.password = password
        self.hostname = hostname
        self.port = port
        self.sid = sid

        connString = username + '/' + password + '@' + hostname + ':' + port + '/' + sid
        self.dbConnection = cx_Oracle.connect(connString)
        self.dbCursor = self.dbConnection.cursor()


    def closeConnection(self):
        self.dbConnection.close()

    def executeQuery(self):
        pass
