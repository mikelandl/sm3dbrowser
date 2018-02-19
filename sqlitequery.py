class SqliteQuery():

    """SQLite query class"""

    def __init__(self, dbConnection, dbCursor):
        """Initialize attributes"""
        self.dbConnection = dbConnection
        self.dbCursor = dbCursor

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


    def build(self):
        pass
