from dbconnection import DBConnection
from dbconnections import DBConnections
from sqliteconnection import SqliteConnection
from excel import Excel
#from pypika import Query, Table, Field

#q = Query.from_('connectioninfo').select('Name','HostName','Port','SID','Username','Password','VPN','Description')
#print(str(q))

#create test database connection
#d = DBConnection(name="test connection20", hostname="127.0.0.1", port=1521, sid="TESTDB", username="user1", password="pass1", vpn=1, description="Test database connection")
#d.addConnection(dbConn, cursor)

#retrieve list of all connections
#c = DBConnections()
#c.loadConnections(cursor)

#create test query
#q = SqliteQuery(dbConn, cursor)
#q.addQuery('select count(*) from queries', 'Mike', 3.4)
#results = q.searchQuery('queries')


configDB = SqliteConnection("/home/mike/projects/python/sm3dbrowser/sm3dbrowser.sqlite")

#results = configDB.searchQuery('queries')
results = configDB.executeQuery("SELECT * FROM connectioninfo",())
#parameters = ('%'+'con'+'%',)
#results = configDB.executeQuery("SELECT * FROM connectioninfo WHERE Name LIKE ?",parameters)
configDB.closeConnection()

xl = Excel('test.xlsx', 'first worksheet')
xl.addWorksheet('Parameters')
xl.writeRows('first worksheet', 1, 1, results)
xl.writeFile()
