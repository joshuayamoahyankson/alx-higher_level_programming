#!/usr/bin/python3
"""A  script that takes in arguments and displays all
values in the states table of hbtn_0e_0_usa where name
matches the argument. But this time,
write one that is safe from MySQL injections!
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

    query = "SELECT * FROM states WHERE name LIKE BINARY '{}' \
            ORDER BY id ASC"
    cursor.execute(query, state_name_searched)
    results = cursor.fetchall()

    for lists in results:
        print(lists)

    cursor.close()
    db.close()
