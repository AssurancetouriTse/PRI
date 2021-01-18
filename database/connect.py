import mysql.connector
from mysql.connector import Error
from configparser  import ConfigParser
import request
import dataConverter
def read_db_config(filename = 'config.ini', section = 'mysql'):
	parser = ConfigParser()
	parser.read(filename)
	db = {}

	if parser.has_section(section):
		items = parser.items(section)
		for item in items :
			db[item[0]] = item[1]
	else :
		raise Exception('{0} not found in the {1} file'.format(section, filename))

	return db


def connect():
	conn = None
	db_conf = read_db_config()
	try :
		conn = mysql.connector.connect(** db_conf)
		if conn.is_connected():
			print ('connecte a la base')

	except Error as e :
		print(e)
	finally :
		return conn
		#There is no finality, now send request

def quit(conn):
	if conn is not None and conn.is_connected():
		conn.close()
		print('Fin de la connection')



if __name__ == '__main__':
	conn =	connect()
	infos = request.getActivity(conn)
print(infos)
#dataConverter.rowToDict(infos)
quit(conn)

