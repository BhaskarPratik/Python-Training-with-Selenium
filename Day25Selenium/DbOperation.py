# ====================Ms sql server connection=======================
# import pyodbc
# conn = pyodbc.connect('Driver={SQL Server};'
#                       'Server=MANGESH-PC;'
#                       'Database=Coforge;'
#                       'Trusted_Connection=yes;')
#
# cursor = conn.cursor()
# cursor.execute("insert into ibm_emp values(128,'Irfan Shambolic','Hr',98100,'Pune')")
# conn.commit()  # commit transaction
# conn.close()
# =================Oracle connection ========================================
import cx_Oracle
import os

insert_query = "insert into city_tbl values(9,'Mumbai') "
update_query = "update city_tbl set cname = 'vashi' where cid = 7"
delete_query = " delete from city_tbl where cid = 8"

try:
    os.environ['PATH'] = 'E:\\instantclient-basic-windows.x64-21.9.0.0.0dbru\\instantclient_21_9'
    conn = cx_Oracle.connect("system", "system", "localhost/xe")
    cursor = conn.cursor()
    cursor.execute(delete_query)
    conn.commit()
    conn.close()
except:
    print("Connection Unsuccessfully")
print("finished")