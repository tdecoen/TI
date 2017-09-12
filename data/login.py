class Login:
    def __init__(self, id, date, sourceip, client, result):
        # constructor
        self.__id = id
        self.__date = date
        self.__sourceip = sourceip
        self.__client = client
        self.__result = result

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, date):
        self.__date = date

    @property
    def sourceip(self):
        return self.__sourceip

    @sourceip.setter
    def sourceip(self, sourceip):
        self.__sourceip = sourceip

    @property
    def client(self):
        return self.__client

    @client.setter
    def client(self, client):
        self.__client = client

    @property
    def result(self):
        return self.__result

    @result.setter
    def result(self, result):
        self.__result = result
