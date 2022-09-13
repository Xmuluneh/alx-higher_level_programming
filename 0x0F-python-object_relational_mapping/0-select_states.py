#!/usr/bin/python3
"""lists all states with a name starting with N
(upper N) from the database hbtn_0e_0_usa"""

if __name__ == '__main__':
    import MySQLdb

    # import sys

    conn = MySQLdb.connect(host="localhost", port=3306,
                           user="root", passwd="passwd123",
                           db="hbtn_0e_0_usa", charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
