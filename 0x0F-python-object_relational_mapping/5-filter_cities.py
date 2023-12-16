#!/usr/bin/python3
""" import MySQLdb """
import MySQLdb
from sys import argv
""" DOC """

if __name__ == "__main__":
    sql_usrname = argv[1]
    sql_pwd = argv[2]
    db = argv[3]
    StateName = argv[4]

    # print(sql_usrname, sql_pwd, db)
    connected = MySQLdb.connect(host="localhost", port=3306,
                                user=sql_usrname, passwd=sql_pwd,
                                db=db, charset="utf8")

    cur = connected.cursor()
    cur.execute(
        "SELECT name FROM cities \
            WHERE state_id = (SELECT id FROM states WHERE name LIKE BINARY %s)\
            ORDER BY cities.id ASC", (StateName, ))
    rows = cur.fetchall()
    tuples = ()
    for row in rows:
        tuples += row
    print(*tuples, sep=", ")
    cur.close()
    connected.close()
