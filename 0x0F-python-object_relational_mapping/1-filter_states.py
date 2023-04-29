#!/usr/bin/python3

""" module - using filter"""
import MySQLdb
from sys import argv

""" using the filter function in mysqldb"""

if __name__ == "__main__":

    db = MySQLdb.connect(
            host="localhost", port=3306, user=argv[1],
            passwd=argv[2], database=argv[3])
    cursor = db.cursor()

    cursor.execute(
            "SELECT * FROM states WHERE name like BINARY 'N%' ORDER BY id ASC")

    states = cursor.fetchall()

    for state in states:
        print(state)
    cursor.close()
    db.close()
