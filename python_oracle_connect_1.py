import cx_Oracle
import os
# os.environ 'PATH' = ''

usern='SCOTT'
pswd='TIGER'
try:
    connection1 = cx_Oracle.connect(user=usern, password=pswd,dsn='localhost/orcl')
    print("Oracle Server Version",connection1.version)
except:
    print("Connection Failed")

try:
    cursor1 = connection1.cursor()
    print("Connected To Oracle DB")
except:
    print("Error Connecting To Oracle DB")

try:
    SQL_QUERY = input("Enter a Valid ORACLE Sql Query : ")
except:
    print(SQL_QUERY,"This Is Not a Valid Query")

try:
    Exicute1=cursor1.execute(SQL_QUERY)
    print("Query Executed Succefully\n")
    connection1.commit()
    try:
        print('Query Result\n')
        for r in Exicute1:
            print(r)
            # row = Exicute1.fetchone()
            # print(row,'\n')
            # row1 = Exicute1.fetchall
            # print(row1)
    except:
        print('No Result')        
except:    
    print('Table Dropped Or Invalid Query')

# try:
#     print(cursor.fetchall())
# except:
#     print("Fetch Failed")

cursor1.close()
connection1.close()