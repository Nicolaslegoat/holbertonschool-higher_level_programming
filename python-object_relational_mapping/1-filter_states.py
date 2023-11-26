#!/usr/bin/python3
"""
Module that lists all states from the database
"""

import MySQLdb
import sys

if __name__ == "__main__":

    if len(sys.argv) != 4:
        exit(1)

    database = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        database=sys.argv[3]
    )

    cursor = database.cursor()

    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id")

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    database.close()
