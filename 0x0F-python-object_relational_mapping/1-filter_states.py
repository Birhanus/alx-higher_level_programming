#!/usr/bin/python3

import MySQLdb
import sys

if __name__ == "__main__":
    """open connection with datatbase"""
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    """perpare a cursor object using cursor() method"""
    cur = db.cursor()
    sql = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id"
   
    """execute the SQL command """
    cur.execute(sql)

    """Fetch the data"""
    results = cur.fetchall()
    for a in results:
        print(a)
    db.close()
