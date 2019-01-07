#encoding=utf-8
from app import GstoreConnector
#!/usr/bin/env python
#import os
#import unittest
import re
from app import app
from json import dumps
from flask import Flask, g, Response, request,jsonify,abort, make_response
#from neo4j.v1 import GraphDatabase, basic_auth
from py2neo import Graph
#from flask_mysqldb import MySQL
#from neo4j import GraphDatabase
import MySQLdb
gc = GstoreConnector.GstoreConnector("10.168.7.245", 9001)
username = "root"
password = "123456"

def queryholders(names,depth):
    curs = db403.cursor()
    nodes = []
    a = []
    for name in names:  #python 字符串连接啊
        sparql = "select distinct * where{<file:///F:/d2r-server-0.7/holder8.nt#holder_copy/" +name+"> <http://localhost:2020/vocab/resource/holder_copy_holder_name> ?t}"
        #print(sparql)
        strr = gc.query(username, password, "holder10", sparql)
        r = strr.split("\n")
        for i in r:
            p = re.compile(r'[\u4e00-\u9fa5]')  # 提取中文
            res = re.findall(p, i)
            result = ''.join(res)
            query = "SELECT * FROM enterprise_copy where name = %s"
            param = (result,)
            curs.execute(query, param)
            rvs = curs.fetchall()
            for t in rvs:
                ids = t[1]
            p = 0
            if len(result) < 4 and len(result) > 1:
                p = 2
                nodes.append({"名称": result, "类型": p,"信用代码":ids})
                a.append(result)
            elif len(result) >= 4:
                p = 1
                nodes.append({"名称": result, "类型": p,"信用代码":ids})
                a.append(result)
    if depth == 1:
        return nodes
    else:
        return queryholders(a, depth - 1)

#print(queryholders(['招商银行股份有限公司'],3))  输入的是一个数组
def queryholders2(names,depth):
    curs = db403.cursor()
    nodes = []
    a = []
    for name in names:  # python 字符串连接啊
        sparql2 = "select distinct * where{ ?x <http://localhost:2020/vocab/resource/holder_copy_holder_name> <file:///F:/d2r-server-0.7/holder8.nt#holder_copy/" + name + ">}"
        strr2 = gc.query(username, password, "holder10", sparql2)
        r2 = strr2.split("\n")
        for i2 in r2:
            p2 = re.compile(r'[\u4e00-\u9fa5]')  # 提取中文
            res2 = re.findall(p2, i2)
            result2 = ''.join(res2)
            query2 = "SELECT * FROM enterprise_copy where name = %s"
            param2 = (result2,)
            curs.execute(query2, param2)
            rv2 = curs.fetchall()
            for t in rv2:
                ids = t[1]
            p2 = 0
            if len(result2) < 4 and len(result2) > 1:
                p2 = 2
                nodes.append({"名称": result2, "类型": p2,"信用代码":ids})
                a.append(result2)
            elif len(result2) >= 4:
                p2 = 1
                nodes.append({"名称": result2, "类型": p2,"信用代码":ids})
                a.append(result2)
    if depth == 1:
        return nodes
    else:
        return queryholders(a, depth - 1)
#print(queryholders2(['招商银行股份有限公司'],2))
def combine(names,depth):
    return queryholders(names,depth)+queryholders2(names,depth)
#print(combine(['招商银行股份有限公司'],1))

#app = Flask(__name__, static_url_path='/static/')
#dbs = MySQLdb.connect("localhost", "root", "zlj000", "zlj")
db403 = MySQLdb.connect("10.168.7.245", "root", "zhirong123", "business_data_db",charset='utf8')  #utf8处理中文
#password = os.getenv("NEO4J_PASSWORD")
#driver = GraphDatabase.driver('bolt://localhost',auth=basic_auth("neo4j", password))
#curs = db403.cursor()
# query = "SELECT * FROM enterprise where id = %s"
# param = "00000029-019c-4c91-86dd-3c20c946d09d"
# curs.execute(query, param)
# curs.execute("SELECT * FROM enterprise where id = %s", ("00000029-019c-4c91-86dd-3c20c946d09d",))
# #curs.execute("SELECT * FROM enterprise where id = '00000029-019c-4c91-86dd-3c20c946d09d'")
# rv = curs.fetchall()
# name = rv[0][0]
# name = [name]
# print(name)
#driver = GraphDatabase.driver("bolt://10.168.7.245:7687", auth=("neo4j", "123456"))
db = Graph("bolt://localhost:7687",password="123456")
# def get_db():
#     if not hasattr(g, 'neo4j_db'):
#         g.neo4j_db = driver.session()
#     return g.neo4j_db
#
# @app.teardown_appcontext
# def close_db(error):
#     if hasattr(g, 'neo4j_db'):
#         g.neo4j_db.close()

@app.route("/")
def get_index():
    #return app.send_static_file('index.html')
    return "he"


def serialize_company(m):
    return {
        'id': m['id'],
        'name': m['name'],
        'stockId': m['stockId'],
    }
def serialize_papers(m):
    return {
        'paperID': m[0],
        'URI': m[1],
        'Title': m[2],
        'Abstract': m[3],
        'Year': m[4],
        'Conference': m[5],
        'Publish': m[6],
    }
def serialize_company(m):
    return {
        '公司唯一识别码': m[0],
        '公司名': m[1],
        '状态': m[2],
        '经营者': m[3],
        '开始时间': m[4],
        '注册码': m[5],
        '注册资本': m[6],
        '企业编码': m[7],
        '信用码': m[8],
        '经营范围': m[9],
        '合伙人': m[10],
        '电话': m[11],
        '企业邮箱': m[12],
        '注册地址': m[13],
        '企业网站': m[14],
        '传真': m[15],
        '员工': m[16],
        '经营许可': m[17],
        '具体经营': m[18],
        '企业类型': m[19],
        '省份': m[20],
        '行业类别': m[21],
        '经营范围大类': m[22],
        '所属机构': m[23],
        '企业地址': m[24],
    }
# def serialize_cast(cast):
#     return {
#         'name': cast[0],
#         'job': cast[1],
#         'role': cast[2]
#     }

@app.route("/mysql")
def get_items():
    curs = dbs.cursor()
    try:
        curs.execute("SELECT * FROM papers")
        rv = curs.fetchall()
    except:
        print ("Error: unable to fetch items")
    return Response(dumps([serialize_papers(record) for record in rv]),
                    mimetype="application/json")
@app.route("/mysql/search")
def mysql_search():
    curs = dbs.cursor()
    try:
        q = request.args["q"]
    except KeyError:
        return []
    else:
        query = "SELECT * FROM papers where PaperID = %s"
        param = q
        curs.execute(query, param)
        rv = curs.fetchall()
    return Response(dumps([serialize_papers(i) for i in rv]),
                    mimetype="application/json")
@app.route("/enterprise", methods=['GET'])
def enterprise_search():
    curs = db403.cursor()
    try:
        id = request.args["id"]
    except KeyError:
        return []
    else:
        query = "SELECT * FROM enterprise where id = %s"
        param = (id,)
        curs.execute(query, param)
        rv = curs.fetchall()
    #return Response(dumps([serialize_company(i) for i in rv]),
                    #mimetype="application/json")
    return dumps([serialize_company(i) for i in rv],ensure_ascii=False)

@app.route("/holder")
def holder_search():
    try:
        name= request.args["name"]
        depth = request.args["depth"]
    except KeyError:
        return []
    else:
        name = [name]  #字符串变成数组
        depth = int(depth)  #字符串变成整型
        #print(type(name))
        a = combine(name,depth)
    #return Response(dumps(a),mimetype="application/json")
    return dumps(a, ensure_ascii=False)
# def holder_search():
#     curs = db403.cursor()
#     try:
#         id = request.args["id"]
#         depth = request.args["depth"]
#     except KeyError:
#         return []
#     else:
#         query = "SELECT * FROM enterprise where id = %s"
#         param = (id,)
#         curs.execute(query, param)
#         rv1 = curs.fetchall()
#         name = rv1[0][1]
#         name = [name]  #字符串变成数组
#         depth = int(depth)  #字符串变成整型
#         #print(type(name))
#         a = combine(name,depth)
#     #return Response(dumps(a),mimetype="application/json")
#     return dumps(a, ensure_ascii=False)

@app.route("/graph")
def get_graph():
    try:
        q = request.args["q"]
    except KeyError:
        return []
    else:
        results = db.run("MATCH (m:Stock)<-[r:CONTAINS]-(a) "
                     "WHERE m.name ={name} "
                     "RETURN m.name as holder, collect(a.name) as company ", {"name": q })
        #print(results)
        nodes = []
        rels = []
        i = 0
        for record in results:
            nodes.append({"name": record["holder"], "label": "holder"})
            target = i
            i += 1
            for name in record['company']:
                company = {"name": name, "label": "company"}
                try:
                    source = nodes.index(company)
                except ValueError:
                    nodes.append(company)
                    source = i
                    i += 1
                rels.append({"source": name, "target": record["holder"],"label": "CONTAINS"})
        return Response(dumps({"nodes": nodes, "links": rels}),
                        mimetype="application/json")

@app.route("/search")
def get_search():
    try:
        q = request.args["q"]
    except KeyError:
        return []
    else:
        #db = get_db()
        results = db.run("MATCH (m:Stock) "
                 "WHERE m.name =~ {name} "
                 "RETURN m", {"name": "(?i).*" + q + ".*"}
        )
        return Response(dumps([serialize_company(record['m']) for record in results]),
                        mimetype="application/json")
@app.route("/level")
def get_level():
    data = db.run("MATCH path=(n1{name:'山东省企业托管经营股份有限公司'})<-[*1..2]-(n2) RETURN path" ).data()
    nodes_source = []
    nodes_target = []
    rels = []
    for record in data:
        pathIdx = 0
        # print(record)
        for path in record['path']:
            # print(path)
            source = path.start_node['name']
            target = path.end_node['name']
            nodes_source.append({"name": source, "category": pathIdx + 1})
            nodes_target.append({"name": target, "category": pathIdx})
            pathIdx += 1
            node = nodes_source + nodes_target
            rels.append({"source": source, "target": target, "label": path['STOCK_PERCENT']})
    #点去重
    temp = []
    [temp.append(i) for i in node if not i in temp]
    return Response(dumps({"nodes": temp, "links": rels}),
                        mimetype="application/json")
@app.route("/level_search")
def get_levelsearch():
    try:
        q = request.args["q"]
        p = request.args["p"]
    except KeyError:
        return []
    else:
        #db = get_db()
        results = db.run("MATCH path = (n1:Stock)<-[r:*1..{p}]-(n2) WHERE n1.name={name} RETURN path",{"name":q,"level":p }).data()
        #db.run("MATCH path=(n1{name:'山东省企业托管经营股份有限公司'})<-[*1..2]-(n2) RETURN path").data()
        #print(results)
        nodes_source = []
        nodes_target = []
        rels = []
        for record in results:
            pathIdx = 0
            # print(record)
            for path in record['path']:
                # print(path)
                source = path.start_node['name']
                target = path.end_node['name']
                nodes_source.append({"name": source, "category": pathIdx + 1})
                nodes_target.append({"name": target, "category": pathIdx})
                pathIdx += 1
                node = nodes_source + nodes_target
                rels.append({"source": source, "target": target, "label": path['STOCK_PERCENT']})
        # 点去重
        temp = []
        [temp.append(i) for i in node if not i in temp]
        return Response(dumps({"nodes": temp, "links": rels}),
                        mimetype="application/json")

@app.route("/movie/<title>")
def get_movie(title):
    #db = get_db()
    results = db.run("MATCH (movie:Movie {title:{title}}) "
             "OPTIONAL MATCH (movie)<-[r]-(person:Person) "
             "RETURN movie.title as title,"
             "collect([person.name, "
             "         head(split(lower(type(r)), '_')), r.roles]) as cast "
             "LIMIT 1", {"title": title})

    result = results.single();
    return Response(dumps({"title": result['title'],
                           "cast": [serialize_cast(member)
                                    for member in result['cast']]}),
                    mimetype="application/json")


# if __name__ == '__main__':
#     app.run(port=8080)


