#!/usr/bin/env python
import psycopg2
import re
import sys
import os

###########################################################################
host="10.10.93.101"
user="postgres"
password="postgres"
dbnameZGMDB="ZGM2.10_ZGMDB_jinpzhang"
dbnameGeneratorZGMDB="ZGM2.10_GeneratorMngDB_jinpzhang"
schemaname='scm_rdnw'
process_code='PROCESS_CODE=10301000000'
###########################################################################

#Connect DB
def OpenDB(dbname,user,password,host):
	connectInfo="dbname="+dbname+" user="+user+" password=" + password + " host=" + host
	print(connectInfo)
	conn = psycopg2.connect(connectInfo)
	return conn

#Close DB
def CloseDB(conn):
	conn.close()

#close cursor
def CloseCur(cur):
	cur.close()

#Open a cursor
def OpenCursor(conn):
	cur = conn.cursor()
	return cur

#Execute a SQL
#def ExecSql(cur,Sql,data):
#	try:
#		cur.execute(Sql,data)
#	except psycopg2.Error , e:
#		print e.pgerror

def GetAlltablesName(cur):
	global listTaleName
	Sql="select tablename from pg_tables where schemaname='" + schemaname +"'"
	print(Sql)
	try:
		cur.execute(Sql)
	except psycopg2.Error,e:
		print e.pgerror
	else:
		for record in cur:
			listTaleName.append(record[0])	
	return listTaleName


def CleanTableData(cur,listTaleName):
	for iTaleName in listTaleName:
		Sql="delete from " + schemaname + "."+ iTaleName +";"
		try:
			cur.execute(Sql)
		except psycopg2.Error,e:
			print e.pgerror
		else:
			print(Sql)

###start### 
if len(sys.argv) > 1:
	if len(sys.argv) == 2:
		if sys.argv[1].find('PROCESS_CODE') != -1:
			if sys.argv[1] != process_code:
				print(sys.argv[1])
				sys.exit(0)
		else:
			print("input process_code parameter ["+sys.argv[1]+"] is error!")
			sys.exit(0)

	else:
		print("Only need one process_code parameter!")
		sys.exit(0)

###clean ZGMDB start###
listTaleName=[]
conn=OpenDB(dbnameZGMDB,user,password,host)
cur=OpenCursor(conn)
listTaleName=GetAlltablesName(cur)
CleanTableData(cur,listTaleName)
conn.commit()
CloseCur(cur)
CloseDB(conn)

###clean GeneratorZGMDB start###
listTaleName=[]
conn=OpenDB(dbnameGeneratorZGMDB,user,password,host)
cur=OpenCursor(conn)
listTaleName=GetAlltablesName(cur)
CleanTableData(cur,listTaleName)
conn.commit()
CloseCur(cur)
CloseDB(conn)

print("Zzzz")
