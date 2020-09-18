class fileOperations:
	def __init__(self , name):
		self.name = name

	def saveInfo(self , name):
		with open(name , 'w+') as infoFile:
			