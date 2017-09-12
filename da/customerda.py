from TI.data import Customer, Login
from .database import connect
from datetime import datetime, timedelta

class CustomerDA:


	def __init__(self):
		self.__db = connect('192.168.0.100', 27017, 'Xwrite', 'ProjectWrite', 'projectx')

	def find(self):
		return self.__db.customers.find()

	def findCompany(self, company):

		result =  self.__db.customers.find_one({'company':company})
		return str(result['sensors'])

	def findUsername(self, username):
		return self.__db.customers.find({'username':username})

	def checkSourceIP(self, sourceip):
		start = datetime.datetime.now() - datetime.timedelta(seconds=1)
		end = datetime.datetime.now() 
		return self.__db.login.find({'sourceip':sourceip, 'date':{'$lt':start,'$gte':end}})
