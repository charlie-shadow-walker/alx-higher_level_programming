#!/usr/bin/python3

""" module - database module"""
import MySQLdb
from sys import argv

"""
a script to list all the states
in a db in ascending order by id"""

if __name__ == '__main__':

    db = MySQLdb.connect(
            host="localhost", port=3306, user=argv[1],
            passwd=argv[2], database=argv[3])

    cursor = db.cursor()

    sql_query = "SELECT * FROM states ORDER BY id ASC"

    cursor.execute(sql_query)

    states = cursor.fetchall()

    for state in states:
        print(state)
    cursor.close()

    db.close()
