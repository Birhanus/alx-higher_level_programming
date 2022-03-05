#!/usr/bin/python3

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM cities JOIN states\
               ON cities.state_id = states.id ORDER BY cities.id")
    [print(", ".join(a[2] for a in cur.fetchall() if a[4] == sys.argv[4]))]
