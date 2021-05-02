
import sqlite3
class dbInteracion():
	def __init__(self,dbName):
		self.dbName = str(dbName)
	def connect(self,tableName):
		self.tableName = str(tableName)
		self.connecting = sqlite3.connect(self.dbName)
		self.cursor = self.connecting.cursor()
		return self.cursor
    def saveNewTopic(self,name,translate,transaltePath):
        dbcomand = "INSERT INTO {0}(title , translate, templateAdress) VALUES({1});".format(self.tableName,tuple(name,translate,transaltePath))
