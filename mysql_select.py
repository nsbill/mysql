# -*- coding: utf-8 -*-
#import sys
#sys.path.insert(0, '/app/db')

from mysql.connector import MySQLConnection, Error
from mysql_db_conf import read_db_config
#from django.shortcuts import render
from datetime import datetime, date, time

def iter_row(cursor, size=10):
    while True:
        rows = cursor.fetchmany(size)
        if not rows:
            break
        for row in rows:
            yield row

def query_with_delete():
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
 #       cursor.execute("SELECT *,from_unixtime(clock) FROM zabbix.history WHERE clock < (UNIX_TIMESTAMP(\"2016-12-31 00:00:01\")) AND itemid IN (SELECT itemid FROM zabbix.items WHERE hostid=10134 OR hostid=10132 OR hostid=10097 OR hostid=10094 OR hostid=10122 OR hostid=10140 OR hostid=10147 OR hostid=10127 OR hostid=10121 OR hostid=10128 OR hostid=10119 OR hostid=10135 OR hostid=10144 OR hostid=10130 OR hostid=10131) LIMIT 10;")
        cursor.execute("DELETE FROM zabbix.history WHERE clock < (UNIX_TIMESTAMP(\"2016-12-31 00:00:01\")) LIMIT 10000;")
        conn.commit()
#        all = {}
#        a = []
#        for row in iter_row(cursor, 10):
#            print(row)

        print('--DELETE--')
        print(str(datetime.now()))

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()
#        return a

    if __name__ == '__main__':
        query_with_delete()

