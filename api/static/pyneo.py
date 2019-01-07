from py2neo import Graph
from json import dumps
from flask import Flask, g, Response, request
graph_3 = Graph("bolt://10.168.7.245:7687",password="123456")
app = Flask(__name__, static_url_path='/static/')
#print(data)
#print(type((data[0]['path']).start_node['name']))
data = graph_3.run("MATCH path=(n1{name:'山东省企业托管经营股份有限公司'})<-[*1..2]-(n2) RETURN path" ).data()
nodes_source = []
nodes_target = []
rels = []

for record in data:
    pathIdx = 0
    #print(record)
    for path in record['path']:
        #print(path)
        source = path.start_node['name']
        target = path.end_node['name']
        nodes_source.append({"name": source,"category": pathIdx+1})
        nodes_target.append({"name": target,"category": pathIdx})
        pathIdx+=1
        node = nodes_source+nodes_target
        rels.append({"source": source, "target": target, "label": path['STOCK_PERCENT']})
#nodes = list(set(node))
#lst2 = {}.fromkeys(node).keys()
temp = []
[temp.append(i) for i in node if not i in temp]
print(temp)
        #print(rels)



