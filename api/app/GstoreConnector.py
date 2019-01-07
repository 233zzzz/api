#encoding=utf-8
import requests
defaultServerIP = "10.168.7.245"
defaultServerPort = "9001"
import re

class GstoreConnector:
    def __init__(self, ip, port):
        if (ip == "10.168.7.245"):
            self.serverIP = defaultServerIP
        else:
            self.serverIP = ip
        self.serverPort = port
        self.Url = "http://" + self.serverIP + ":" + str(self.serverPort)

    def UrlEncode(self, s):
        ret = ""
        for i in range(len(s)):
            c = s[i]
            if ((ord(c) == 42) or (ord(c) == 45) or (ord(c) == 46) or (ord(c) == 47) or (ord(c) == 58) or (
                    ord(c) == 95)):
                ret += c
            elif ((ord(c) >= 48) and (ord(c) <= 57)):
                ret += c
            elif ((ord(c) >= 65) and (ord(c) <= 90)):
                ret += c
            elif ((ord(c) >= 97) and (ord(c) <= 122)):
                ret += c
            elif (ord(c) >= 256):
                ret += chr(ord(c))
            elif ((ord(c) != 9) and (ord(c) != 10) and (ord(c) != 13)):
                ret += "{}{:X}".format("%", ord(c))
        return ret

    def Get(self, strUrl):
        r = requests.get(self.UrlEncode(strUrl))
        return r.text

    def fGet(self, strUrl, filename):
        r = requests.get(self.UrlEncode(strUrl), stream=True)
        with open(filename, 'wb') as fd:
            for chunk in r.iter_content(4096):
                fd.write(chunk)
        return

    def load(self, db_name, username, password):
        cmd = self.Url + "/?operation=load&db_name=" + db_name + "&username=" + username + "&password=" + password
        res = self.Get(cmd)
        print(res)
        if res == "load database done.":
            return True
        return False

    def unload(self, db_name, username, password):
        cmd = self.Url + "/?operation=unload&db_name=" + db_name + "&username=" + username + "&password=" + password
        res = self.Get(cmd)
        print(res)
        if res == "unload database done.":
            return True
        return False

    def build(self, db_name, rdf_file_path, username, password):
        cmd = self.Url + "/?operation=build&db_name=" + db_name + "&ds_path=" + rdf_file_path + "&username=" + username + "&password=" + password
        res = self.Get(cmd)
        print(res)
        if res == "import RDF file to database done.":
            return True
        return False

    def query(self, username, password, db_name, sparql):
        cmd = self.Url + "/?operation=query&username=" + username + "&password=" + password + "&db_name=" + db_name + "&format=test&sparql=" + sparql
        return self.Get(cmd)

    def fquery(self, username, password, db_name, sparql, filename):
        cmd = self.Url + "/?operation=query&username=" + username + "&password=" + password + "&db_name=" + db_name + "&format=json&sparql=" + sparql
        self.fGet(cmd, filename)
        return

    def show(self, username, password):
        cmd = self.Url + "/?operation=show&username=" + username + "&password=" + password
        return self.Get(cmd)

    def user(self, type, username1, password1, username2, addition):
        cmd = self.Url + "/?operation=user&type=" + type + "&username1=" + username1 + "&password1=" + password1 + "&username2=" + username2 + "&addition=" + addition
        return self.Get(cmd)

    def showUser(self):
        cmd = self.Url + "/?operation=showUser"
        return self.Get(cmd)

    def monitor(self, db_name, username, password):
        cmd = self.Url + "/?operation=monitor&db_name=" + db_name + "&username=" + username + "&password=" + password
        return self.Get(cmd)

    def checkpoint(self, db_name, username, password):
        cmd = self.Url + "/?operation=checkpoint&db_name=" + db_name + "&username=" + username + "&password=" + password
        return self.Get(cmd)
gc =  GstoreConnector("10.168.7.245", 9001)
username = "root"
password = "123456"
# sparql = "select distinct * where{<file:///F:/d2r-server-0.7/holder8.nt#holder_copy/招商银行股份有限公司>  <http://localhost:2020/vocab/resource/holder_copy_holder_name> ?t}"
# filename = "res.txt"
# strr = gc.query(username, password, "holder10", sparql)
# nodes = []
# a = []
# r = strr.split("\n")
# for i in r:
#     #print(type(i))
#     p = re.compile(r'[\u4e00-\u9fa5]')  # 提取中文
#     res = re.findall(p, i)
#     #print(res)
#     result = ''.join(res)
#     #print(result)
#     #print(len(result))
#     p = 0
#     if len(result) < 4 and len(result) > 1:
#         p = 2
#         nodes.append({"名称": result, "类型": p})
#         a.append(result)
#     elif len(result) >= 4:
#         p = 1
#         nodes.append({"名称": result, "类型": p})
#         a.append(result)
# print(a)
#print(nodes)
# node1 = []
# b = []
# for i in a:
#     #print(type(i))
#     sparql = "select * where{<file:///F:/d2r-server-0.7/holder8.nt#holder_copy/{i}  <http://localhost:2020/vocab/resource/holder_copy_holder_name> ?t}", {
#         "i": i}
#     strr = gc.query(username, password, "holder10", sparql)
#     r = strr.split("\n")
#     print(r)
#     for i in r:
#         p = re.compile(r'[\u4e00-\u9fa5]')  # 提取中文
#         res = re.findall(p, i)
#         result = ''.join(res)
#         p = 0
#         if len(result) < 4 and len(result) > 1:
#             p = 2
#             node1.append({"名称": result, "类型": p})
#             b.append(result)
#         elif len(result) >= 4:
#             p = 1
#             node1.append({"名称": result, "类型": p})
#             b.append(result)
#print(b)



#print(res)
#print(gc.UrlEncode("http://10.168.7.245:9001/?operation&db_name=lubm&username=root&password=123456"))

def queryholders(names,depth):
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
            p = 0
            if len(result) < 4 and len(result) > 1:
                p = 2
                nodes.append({"名称": result, "类型": p})
                a.append(result)
            elif len(result) >= 4:
                p = 1
                nodes.append({"名称": result, "类型": p})
                a.append(result)
    if depth == 1:
        return nodes
    else:
        return queryholders(a, depth - 1)

#print(queryholders(['招商银行股份有限公司'],3))
def queryholders2(names,depth):
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
            p2 = 0
            if len(result2) < 4 and len(result2) > 1:
                p2 = 2
                nodes.append({"名称": result2, "类型": p2})
                a.append(result2)
            elif len(result2) >= 4:
                p2 = 1
                nodes.append({"名称": result2, "类型": p2})
                a.append(result2)
    if depth == 1:
        return nodes
    else:
        return queryholders(a, depth - 1)
#print(queryholders2(['招商银行股份有限公司'],2))
def combine(names,depth):
    return queryholders(names,depth)+queryholders2(names,depth)
#print(combine(['招商银行股份有限公司'],1))


