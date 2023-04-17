#!/usr/bin/python3


'''
lists all states with name that startswith  N
from the database hbtn_0e_0_usa
'''
import MySQLdb
from sys import argv
if __name__ == "__main__":
    conn = MySQLdb.connect(
        host="localhost", port=3306, user=argv[1],
        password=argv[2], database=argv[3])
    cursor = conn.cursor()
    cursor.execute(
            "SELECT * FROM states WHERE name LIKE BINARY 'N%'ORDER BY id ASC")
    db = cursor.fetchall()
    for x in db:
        print(x)
