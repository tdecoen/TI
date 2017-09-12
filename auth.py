# -*- coding: utf-8 -*-

from pyrad.client import Client
from pyrad.dictionary import Dictionary
import pyrad.packet
from .mschap2 import MSCHAP2
import six


def radiusAuth(server, secret, username, password, identifier):
	srv = Client(server=server, secret=secret, dict=Dictionary("TI/dicts/dictionary"))
	req = srv.CreateAuthPacket(code=pyrad.packet.AccessRequest, User_Name=username)
	req["NAS-Identifier"] = identifier

	auth = MSCHAP2()
	authAttrs = auth.getAuthAttrs(username, password)
	for key in authAttrs.keys():
		req[key] = authAttrs[key]

	reply = srv.SendPacket(req)

	if reply.code == pyrad.packet.AccessAccept:
		return "Accept"
	else:
		return "Reject"


def verifyPassword(username, password):
	secret = six.b('yCgcNJK')
	return radiusAuth('192.168.0.101', secret, username, password, 'projectx')


def verifyToken(username, token):
	return True


def authenticate(username, password, token, source):
	# sanitize data

	# check if source ip is blocked
	# careful not to block ip for all users if multiple users login from same source ip
	if source != '127.0.0.1': return "False"

	# check if username exists and is not suspended
	if username != 'tdecoen': return "False"

	# check username/token
	if verifyToken(username, token): pass

	# check username/password
	# get role information
	return verifyPassword(username, password)

	# update user login, status and count

	return "Success"
