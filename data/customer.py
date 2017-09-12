class Customer:
	def __init__(self, id, company, status):
		#Constructor
		self.__id = id
		self.__company = company
		self.__status = status

	@property
	def is_authenticated(self): return True

	@property
	def is_active(self): return True

	@property
	def is_anonymous(self): return False

	def get_id(self):
		try:
			return unicode(self.__id)
		except NameError:
			return str(self.__id)
	@property
	def company(self):
		return self.__company

	@company.setter
	def company(self, company):
		self.__company = company

	@property
	def status(self):
		return self.__status

	@status.setter
	def status(self, status):
		self.__status = status

	def __repr__(self):
		return  '<Company %s>' % (self.company)
