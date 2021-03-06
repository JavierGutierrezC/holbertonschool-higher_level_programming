#!/usr/bin/python3
"""script that lists all states from the database hbtn_0e_0_usa"""
import MySQLdb
from sys import argv

if __name__ == '__main__':
    javi_db = MySQLdb.connect(
        host='localhost',
        user=argv[1],
        password=argv[2],
        database=argv[3],
        port=3306)
    cur = javi_db.cursor()

    cur.execute("SELECT id, name FROM states ORDER BY id ASC")
    """rows = cur.fetchall()"""
    for row in cur.fetchall():
        print(row)
    javi_db.close()
    cur.close()
