#!/usr/bin/python3
"""script that lists all states from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys

if __name__ == "__main__":
    """Open databse connnection"""
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    """ prepare a cursor object using cursor() method"""
    cur = db.cursor()

    sql = "SELECT * FROM states ORDER BY id"

    cur.execute(sql)
    """ Fetch all the rows in a list of list"""
    results = cur.fetchall()
    for a in results:
        print(a)
    """disconnect from server"""
    db.close()
