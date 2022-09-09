#!/usr/bin/python3
"""module that lists all states in hbtn_0e_0_usa databse"""

import MySQLdb


conn = MySQLdb.connect(host="localhost", port=3306, user='root', passwd="root", db='my_db', chracter="uft8")
cur = conn.cursor()
cur.excute("SELECT * FROM states ORDER BY id")
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()
