import mysql.connector
db=mysql.connector.connect(user='root',password='',host='127.0.0.1',database='maitreyi')
cursor=db.cursor()
choice=int(input('1.Search students enrolled in a particular course and faculty \n2. Search attendance of a particular student \n3. Enter choice:  '))
if(choice==1):
    

    CID=input('Enter CID of record to search for: ')
    sql="SELECT C.CID,SID,SNAME,TNAME FROM COURSE C,STUDENT S ,TEACHER T  WHERE C.CID=S.CID AND S.CID=T.CID AND C.CID='%s'"%CID

    cursor.execute(sql)
    results=cursor.fetchall()
    print(str.center('CID',10),str.center('SID',10),str.center('SNAME',10),str.center('TNAME',10))
    for row in results:
        print(str.center(row[0],10),str.center(row[1],10),str.center(row[2],10),str.center(row[3],10))

elif(choice==2):
    
    search=input("Do you want to search this person's attendance? Enter SID:   ")

    sql2="SELECT S.SID,SNAME,CID,DATE,STATUS,START_TIME,END_TIME FROM STUDENT S , ATTENDANCE A WHERE  A.SID=S.SID AND A.SID='%s'"%search
    cursor.execute(sql2)
    results=cursor.fetchall()
    print(str.center('SID',10),str.center('SNAME',10),str.center('CID',10),str.center('DATE',10),str.center('STATUS',10),str.center('START_TIME',10),str.center('END_TIME',10))
    for row in results:
        print(str.center(row[0],10),str.center(row[1],10),str.center(row[2],10),str.center(str(row[3]),10),str.center(row[4],10),str.center(str(row[5]),10),str.center(str(row[6]),10))

        
        
db.close()




