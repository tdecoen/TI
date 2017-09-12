from pymongo import MongoClient
import ssl

def connect(host, port, username, password, database):
	connection = MongoClient(host, port, ssl=True, ssl_cert_reqs=ssl.CERT_NONE)
	handle = connection[database]
	handle.authenticate(username, password)
	return handle



