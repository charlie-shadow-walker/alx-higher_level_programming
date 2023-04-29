#!/usr/bin/python3

"""module - name matching argument"""

import MySQLdb
from sys import argv

"""
a program to return things matching the
passed parameter"""

if __name__ == "__main__":

    db = MySQLdb.connect(
            host="localhost", port=3306, user=argv[1],
            passwd=argv[2], database=argv[3])
    cursor = db.cursor()
    cursor.execute(
            "SELECT * FROM states WHERE name like BINARY"
            "'{:s}' ORDER BY id ASC".format(argv[4]))
    states = cursor.fetchall()
    for state in states:
        print(state)
    cursor.close()
    db.close()

