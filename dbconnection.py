class DBConnection():

    """Database connection info for a specific database"""

    def __init__(self, name, hostname, port, sid, username, password, vpn, description):
        """Initialize attributes"""
        self.name = name
        self.hostname = hostname
        self.port = port
        self.sid = sid
        self.username = username
        self.password = password
        self.vpn = vpn
        self.description = description

    def addConnection(self, dbConnection, dbCursor):
        """Write connection object to 'connectioninfo' table"""

        parameters = [self.name, self.hostname, self.port, self.sid, self.username, self.password, self.vpn, self.description]

        sql = ''' INSERT INTO sites (Name, HostName, Port, SID, Username, Password, VPN, Description) VALUES (?,?,?,?,?,?,?,?) '''

        dbCursor.execute(sql, parameters)
        dbConnection.commit()
