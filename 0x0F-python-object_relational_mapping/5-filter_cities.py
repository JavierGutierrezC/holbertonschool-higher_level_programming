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

    cur.execute("SELECT cities.name FROM states \
    JOIN cities ON cities.state_id = states.id WHERE states.name = %s\
    ORDER by cities.id", [argv[4]])
    new = []
    for row in cur.fetchall():
        new += row
    print(', '.join(new))
    javi_db.close()
    cur.close()
