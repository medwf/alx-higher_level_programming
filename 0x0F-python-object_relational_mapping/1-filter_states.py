#!/usr/bin/python3
""" import MySQLdb """
import MySQLdb
from sys import argv
""" DOC """

if __name__ == "__main__":
    sql_usrname = argv[1]
    sql_pwd = argv[2]
    db = argv[3]

    # print(sql_usrname, sql_pwd, db)
    connected = MySQLdb.connect(host="localhost", port=3306,
                                user=sql_usrname, passwd=sql_pwd,
                                db=db, charset="utf8")

    cur = connected.cursor()
    cur.execute(
        "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    connected.close()
