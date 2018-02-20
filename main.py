from dbconnection import DBConnection
from dbconnections import DBConnections
#from pypika import Query, Table, Field

import sqlite3

dbFile = "/home/mike/projects/python/sm3dbrowser/sm3dbrowser.sqlite"

#test


#q = Query.from_('connectioninfo').select('Name','HostName','Port','SID','Username','Password','VPN','Description')
#print(str(q))



#with sqlite3.connect(dbFile) as dbConn:
#	cursor = dbConn.cursor()


#create test database connection
#d = DBConnection(name="test connection20", hostname="127.0.0.1", port=1521, sid="TESTDB", username="user1", password="pass1", vpn=1, description="Test database connection")
#d.addConnection(dbConn, cursor)

#retrieve list of all connections
#c = DBConnections()
#c.loadConnections(cursor)
