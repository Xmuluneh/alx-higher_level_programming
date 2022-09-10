#!/usr/bin/python3
"""module that lists all states in hbtn_0e_0_usa databse"""
if __name__ == '__main__':
    import MySQLdb
    import sys

conn = MySQLdb.connect(host="localhost", port=3306,
                       user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
cur = conn.cursor()
cur.excute("SELECT * FROM states ORDER BY id")
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()
