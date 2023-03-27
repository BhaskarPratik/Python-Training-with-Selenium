import cx_Oracle
import os

try:
    os.environ['PATH'] = 'E:\\instantclient-basic-windows.x64-21.9.0.0.0dbru\\instantclient_21_9'
    conn = cx_Oracle.connect("system", "system", "localhost/xe")
    cursor = conn.cursor()
    cursor.execute("select * from amodocs_emp")
    for row in cursor:
        print(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
    conn.close()
except:
    print("connection unsuccessfully")
print("finished")