import sqlite3

class SqliteConnection():

    """SQLite connection class"""

    def __init__(self, dbFile):
        """Initialize attributes"""
        self.dbConnection = sqlite3.connect(dbFile)
        self.dbCursor = self.dbConnection.cursor()


    def closeConnection(self):
        self.dbConnection.close()


    def addQuery(self, querySQL, author, sm3version):
        """Write query object to 'queries' table"""

        parameters = (querySQL, author, sm3version)

        sql = ''' INSERT INTO queries (QuerySQL, Author, SM3Version) VALUES (?,?,?) '''

        self.dbCursor.execute(sql, parameters)
        self.dbConnection.commit()


    def getQuery(self):
        pass

    def executeQuery(self):
        pass

    def searchQuery(self, searchString):
        """Find all queries that contain 'searchString'"""

        parameters = ('%'+searchString+'%',)

        sql = "SELECT * FROM queries WHERE QuerySQL LIKE ?"

        self.dbCursor.execute(sql, parameters)

        return self.dbCursor.fetchall()
