import cx_Oracle

usern='SCOTT'
pswd='TIGER'
try:
    conn = cx_Oracle.connect(user=usern, password=pswd,dsn='localhost/orcl')
    print("Oracle Server Version",conn.version)
except:
    print("Connection Failed")

try:
    c = conn.cursor()
    print("Connected To Oracle DB")
except:
    print("Error Connecting To Oracle DB")

try:
    SQL_QRY = input("Enter a Valid ORACLE Sql Queary : ")
except:
    print(SQL_QRY,"This Is Not a Valid Queary")

try:
    d=c.execute(SQL_QRY)
    print("Queary Executed Succefully\n")
    conn.commit()
    try:
        print('Query Result\n')
        for r in d:
            # print(r)
            row = d.fetchone()
            print(row,'\n')
    except:
        print('No Result')        
except:    
    print('Table Dropped Or Invalid Query')

# try:
#     print(cursor.fetchall())
# except:
#     print("Fetch Failed")

c.close()
conn.close()