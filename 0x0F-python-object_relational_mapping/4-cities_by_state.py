#!/usr/bin/python3
"""A script that lists all cities from the database hbtn_0e_4_usa"""

import MySQLdb
import sys


if __name__ == "__main__":
    """Connect to the database and
    retrieve the needed information
    """
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    db = MySQLdb.connect(host="localhost", user=mysql_username,
                         passwd=mysql_password,
                         db=database_name, port=3306)
    cursor = db.cursor()

    query = "SELECT cities.id, cities.name, states.name \
                FROM cities JOIN states ON cities.state_id \
                = states.id ORDER BY cities.id ASC"
    cursor.execute(query)
    results = cursor.fetchall()

    for lists in results:
        print(lists)

    cursor.close()
    db.close()
