#!/usr/bin/python3

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM \
                 hbtn_0e_4_usa.cities JOIN states ON\
                 cities.state_id = states.id ORDER BY cities.id")
    results = cur.fetchall()
    for a in results:
        print(a)
    db.close()
