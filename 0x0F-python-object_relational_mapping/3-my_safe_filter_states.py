#!/usr/bin/python3

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name=%s;", (sys.argv[4],))
    results = cur.fetchall()
    for a in results:
        print(a)
    db.close()
