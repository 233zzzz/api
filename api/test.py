# from json import dumps
# #from flask import Flask, g, Response, request
# #from neo4j.v1 import GraphDatabase, basic_auth
# from neo4j import GraphDatabase
# driver = GraphDatabase.driver("bolt://10.168.7.245:7687", auth=("neo4j", "123456"))
# def get_db():
#     if not hasattr(g, 'neo4j_db'):
#         g.neo4j_db = driver.session()
#     return g.neo4j_db
# db = get_db()
# results = db.run(
# "MATCH path = (n1{name =潍柴动力股份有限公司}) < -[*1..2] - (n2)"
# "UNWIND NODES(path) AS n"
# "WITH path,"
# "SIZE(COLLECT(DISTINCTn)) AS testLength"
# "WHERE testLength = LENGTH(path) + 1"
# "RETURN path, length(path)"
#  )
#
# print(results)
#     # with open("C:/Users/zlj/Desktop/douban.txt", "w") as f:
#     #     f.write(results)
#!/usr/bin/env python
import os
import unittest
from json import dumps
from flask import Flask, g, Response, request,jsonify,abort, make_response
#from neo4j.v1 import GraphDatabase, basic_auth
from py2neo import Graph
from flask_mysqldb import MySQL
#from neo4j import GraphDatabase
import MySQLdb
app = Flask(__name__, static_url_path='/static/')
dbs = MySQLdb.connect("localhost", "root", "zlj000", "zlj")

#password = os.getenv("NEO4J_PASSWORD")
#driver = GraphDatabase.driver('bolt://localhost',auth=basic_auth("neo4j", password))

#driver = GraphDatabase.driver("bolt://10.168.7.245:7687", auth=("neo4j", "123456"))
db = Graph("bolt://localhost:7687",password="123456")
curs = dbs.cursor()
curs.execute("SELECT * FROM papers where PaperID = 1")
rv = curs.fetchall()
print(rv)
for i in rv:
    print(i)
#print(rv)
#print(type(str(rv)))