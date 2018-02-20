from dbconnection import DBConnection
from sqliteconnection import SqliteConnection
from oracleconnection import OracleConnection
from excel import Excel
#from pypika import Query, Table, Field

#build query using pypika
#q = Query.from_('connectioninfo').select('Name','HostName','Port','SID','Username','Password','VPN','Description')
#print(str(q))




#create test database connection
#d = DBConnection(name="test connection20", hostname="127.0.0.1", port=1521, sid="TESTDB", username="user1", password="pass1", vpn=1, description="Test database connection")
#d.addConnection(dbConn, cursor)


#create test query
#q = SqliteQuery(dbConn, cursor)
#q.addQuery('select count(*) from queries', 'Mike', 3.4)
#results = q.searchQuery('queries')



#sqlite
#configDB = SqliteConnection("/home/mike/projects/python/sm3dbrowser/sm3dbrowser.sqlite")
#results = configDB.searchQuery('queries')
#results = configDB.executeQuery("SELECT * FROM connectioninfo",())
#parameters = ('%'+'con'+'%',)
#results = configDB.executeQuery("SELECT * FROM connectioninfo WHERE Name LIKE ?",parameters)
#configDB.closeConnection()

#Oracle
clientDB = OracleConnection('sm3','sm3','192.168.2.115','1521','sm3')
#results = clientDB.executeQuery('SELECT * FROM sha_mst',{})
parameters = {'warehouse_code': '20'}
results = clientDB.executeQuery('SELECT * FROM OEH_HDR WHERE warehouse_code = :warehouse_code', parameters)
clientDB.closeConnection()

xl = Excel('test.xlsx', 'first worksheet')
xl.addWorksheet('Parameters')

#headings = ('ConnectionInfoID','Name','HostName','Port','SID','Username','Password','VPN','Description')
#xl.writeRow('first worksheet', 1, 1, True, headings)
xl.writeRows('first worksheet', 2, 1, False, results)
xl.writeFile()
