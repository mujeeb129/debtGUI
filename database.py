import sqlite3


class SetUp:
	def __init__(self , db):
		self.conn = sqlite3.connect(db)
		self.c = self.conn.cursor()
		self.c.execute("""CREATE TABLE IF NOT EXISTS debtbox(
						  id INTEGER PRIMARY KEY ,
						  name TEXT ,
						  amount INTEGER ,
						  instance TEXT)""")
		self.conn.commit()

	def fetch(self):
		self.c.execute("SELECT * FROM debtbox")
		rows = self.c.fetchall()
		self.conn.commit()
		return rows

	def insert(self , name , amount , instance):
		self.c.execute("INSERT INTO debtbox VALUES(NULL , ? , ? , ?)",(name , amount , instance))
		self.conn.commit()

	def update(self ,id , name , amount , instance):
		self.c.execute("""UPDATE debtbox
						  SET name = ? , amount = ? , instance = ?
						  WHERE id = ?""",(name , amount , instance , id))
		self.conn.commit()

	def delete(self , id):
		self.c.execute("DELETE FROM debtbox WHERE id = ?",(id,))
		self.conn.commit()

	def __del__(self):
		self.conn.close()			