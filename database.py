import sqlite3

class build():
	def __init__(self , database :str):
		'''
		This Class takes the name/path of the database to create and gives a few methods
		to build the basic structure of the database.
		'''
		try:
			self.database = database
			sqlite3.connect(f'{self.database}')
		except:
			return 'Unable to connect to database'		
	def tableio(self ,structure : str ):
		'''
		This function takes the SQL command to create the table
		'''
		try:
			db = sqlite3.connect(f'{self.database}')
			cur = db.cursor()
			cur.execute(f'{structure}')
			db.commit()
			db.close()
		except:
			return 'Unable to process database'
	def structure(self):
		'''
		This function returns the tables in the database.
		'''
		try:
			db = sqlite3.connect(f'{self.database}')
			cur = db.cursor()
			tables = cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
			db.commit()
			db.close()
			return tables
		except:
			return 'Unable to process database'
	def tab_structure(self , table : str):
		'''
		This function returns an iterator with complete stucture of the table
		'''
		try:
			db = sqlite3.connect(f'{self.database}')
			cur = db.cursor()
			meta = cursor.execute(f"PRAGMA table_info('{table}')")
			db.commit()
			db.close()
			return meta
		except:
			return 'Unable to process database'

class manage():
	def __init__(self , database : str):
		'''
		This Class takes the database path and provides many functions
		to manage that database.
		'''
		self.database = database
	def get_all(self , table : str):
		'''
		This Function takes table name and returns an iterator 
		with all the records in the table.
		'''
		try:
			db = sqlite3.connect(f'{self.database}')
			cur = db.cursor()
			
			records = cur.execute(f"SELECT * FROM {table}").fetchall()
			db.commit()
			db.close()
			return records
		except:
			return 'Failed to execut command properly'
	def put_record(self , table : str, data : tuple):
		'''
		This function takes the table name in the database initialised previosly
		and puts the data from the tuple taken as input.
		'''
		try:
			db = sqlite3.connect(f'{self.database}')
			cur = db.cursor()
			cur.execute(f"INSERT INTO {table} VALUES "+data)
			db.commit()
			db.close()
			return 'record put'
		except:
			return 'Failed to execute command properly'
	def query(self , table :str ,query : str ):
		'''
		This function is used to run a direct sql query/command , and returns 
		an iterator to get the results of the query.
		'''
		try:
			db = sqlite3.connect(f'{self.database}')
			cur = db.cursor()
			quired_data = cur.execute(f'{query}')
			db.commit()
			db.close()
			return quired_data
		except:
			return 'Failed to execute command properly'

	def delete(self , query : str):
		'''
		This Function is used to delete a record or a whole table from a database
		For this function to work , you need to provide proper SQL command to delete 
		This function secure and will not execute any sql command / query other than
		deletion or dropping table.
		###_____Warning: Once deleted , the record/table will not be recoverable____###
		'''
		try:
			if query[:6] == 'DELETE' or query[:4] == 'DROP':
				db = sqlite3.connect(f'{self.database}')
				cur = db.cursor()
				cur.execute(f'{query}')
				db.commit()
				db.close()
			else:
				return 'Invalid Deletion Query'
		except:
			return 'Failed to execute command properly'


