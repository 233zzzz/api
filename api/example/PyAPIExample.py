import sys
sys.path.append('../src')
import GstoreConnector

# before you run this example, make sure that you have started up ghttp service (using bin/ghttp db_name port)
username = "root"
password = "123456"
sparql = "select ?x where \
                 { \
                     ?x  <rdf:type> <ub:UndergraduateStudent>. \
                     ?y    <ub:name> <Course1>. \
                     ?x    <ub:takesCourse>  ?y. \
                     ?z   <ub:teacherOf>    ?y. \
                     ?z    <ub:name> <FullProfessor1>. \
                     ?z    <ub:worksFor>    ?w. \
                     ?w    <ub:name>    <Department0>. \
                 }"
sparql2 = "select * where { ?x  ?y  ?z }"

filename = "res.txt"

# start a gc with given IP and Port
gc =  GstoreConnector.GstoreConnector("10.168.7.245", 9001)

# unload the database
#ret = gc.unload("test", username, password)

# build database with a RDF graph
# ret = gc.build("lubm", "data/lubm/lubm.nt", username, password)

# load the database
# ret = gc.load("lubm", username, password)
#
# # show
# print(gc.show(username, password))
#
# # show information of all users
# print(gc.showUser())
#
# # monitor the database status
# print(gc.monitor('lubm', username, password))
#
# # save the database
# print(gc.checkpoint('lubm', username, password))
#
# # query
print(gc.query(username, password, "lubm", sparql))
#
# # query and save the result in a file
# gc.fquery(username, password, "lubm", sparql, filename)