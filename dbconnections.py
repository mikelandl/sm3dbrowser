class DBConnections():
	"""List of 'DBConnection' objects"""

	def __init__(self):
		"""Initialize attributes"""
		self.connections = []

	def loadConnections(self, dbCursor):
		"""Retrieve list of all records in 'connectioninfo' table"""
		dbCursor.execute('SELECT * FROM connectioninfo')
		self.connections=dbCursor.fetchall()
		for connection in self.connections:
			print(connection)
