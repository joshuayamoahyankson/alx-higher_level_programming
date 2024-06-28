#!/usr/bin/python3
"""A script that takes in an argument and
displays all values in the states...
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
    state_name_searched = sys.argv[4]

    db = MySQLdb.connect(host="localhost", user=mysql_username,
                         passwd=mysql_password,
                         db=database_name, port=3306)
    cursor = db.cursor()

    query = "SELECT * FROM states WHERE name = {} \
            ORDER BY id ASC".format(state_name_searched)
    cursor.execute(query)
    results = cursor.fetchall()

    for lists in results:
        print(lists)

    cursor.close()
    db.close()
