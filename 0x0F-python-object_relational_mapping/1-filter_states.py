#!/usr/bin/python3
"""lists all states with a name starting with N
(upper N) from the database hbtn_0e_0_usa"""

if __name__ == '__main__':

    import MySQLdb
    import sys
    user = sys.argv[1]
    passwd = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(host='localhost', port=3306,
                         user="root", passwd="passwd123", db=database)

    cur = db.cursor()
    cur.execute("""SELECT * FROM states WHERE name
                LIKE BINARY 'N%' ORDER BY states.id ASC""")
    rows = cur.fetchall()
    for row in rows:
        print(row)
