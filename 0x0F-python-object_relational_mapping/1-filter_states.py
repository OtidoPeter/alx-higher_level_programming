#!/usr/bin/python3
"""lists all states with a name starting\
    with N (upper N) from the database\
    hbtn_0e_0_usa
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    conn = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        charset='utf8'
    )

    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    names = cur.fetchall()

    for name in names:
        if name[1][0] == 'N':
            print(name)

    cur.close()
    conn.close()
