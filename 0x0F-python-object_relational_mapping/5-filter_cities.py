#!/usr/bin/python3
"""A script that takes in the name of a 
state as an argument and lists all cities
of that state, using the database hbtn_0e_4_usa
"""

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

    query = "SELECT cities.id, cities.name, states.name" + \
                "FROM cities JOIN states ON cities.state_id" + \
                "= states.id WHERE states.name LIKE BINARY '{}' " + \
                "ORDER BY cities.id ASC".format(sys.argv[4])
    cursor.execute(query)
    results = cursor.fetchall()

    for lists in results:
        print(lists)

    cursor.close()
    db.close()
