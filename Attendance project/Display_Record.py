print("Displaying records....")

import mysql.connector
db=mysql.connector.connect(user='root',password='',host='127.0.0.1',database='maitreyi')
cursor=db.cursor()
ans='yes'
while(ans=='yes'):
    choice=int(input("\n1. Display Course \n2. Display Student \n3. Display Attendance  \n4. Enter budget \n5.Display Teacher \n6.Enter Choice:  "))
    if(choice==1):
        sql="SELECT * FROM COURSE"
        try:
            cursor.execute(sql)
            results=cursor.fetchall()
            print(str.center('CID',10),str.center('CNAME',10),str.center('DURATION',10),str.center('FEES',10)) 
            for row in results:
                print(str.center(row[0],10),str.center(row[1],10),str.center(str(row[2]),10),str.center(str(row[3]),10))
                
                          

        except:
            print("Output Error")
    elif(choice==2):
        sql="SELECT * FROM STUDENT"
        try:
            cursor.execute(sql)
            results=cursor.fetchall()
            print(str.center('SID',10),str.center('SNAME',10),str.center('CID',10),str.center('MARKS',10),str.center('GRADE',10)) 
            for row in results:
                print(str.center(row[0],10),str.center(row[1],10),str.center(str(row[2]),10),str.center(str(row[3]),10),str.center(str(row[4]),10))   
                

        except:
            print("Output Error")
    elif(choice==3):
        sql="SELECT * FROM ATTENDANCE"
        try:
            cursor.execute(sql)
            results=cursor.fetchall()
            print(str.center('SL_NO',10),str.center('SID',10),str.center('DATE',10),str.center('STATUS',10),str.center('START_TIME',10),str.center('END_TIME',10)) 
            for row in results:
                print(str.center(str(row[0]),10),str.center(row[1],10),str.center(str(row[2]),10),str.center(str(row[3]),10),str.center(str(row[4]),10),str.center(str(row[5]),10))   
                

        except:
            print("Output Error")

    elif(choice==4):
        print("Courses in  your budget are....")
        budget=int(input("Enter budget: "))
        sql="SELECT * FROM  `course` WHERE FEES <=%d"%budget
        try:
            cursor.execute(sql)
            results=cursor.fetchall()
            print(str.center('CID',10),str.center('CNAME',10),str.center('DURATION',10),str.center('FEES',10)) 
            for row in results:
                print(str.center(row[0],10),str.center(row[1],10),str.center(str(row[2]),10),str.center(str(row[3]),10))
        except:
            print("Error")
    
    elif(choice==5):
        
        sql="SELECT * FROM  TEACHER"
        try:
            cursor.execute(sql)
            results=cursor.fetchall()
            print(str.center('TID',10),str.center('TNAME',10),str.center('CID',30)) 
            for row in results:
                print(str.center(row[0],10),str.center(row[1],10),str.center(str(row[2]),30))
        except:
            print("Error")
    ans=input("Wanna enter another choice? ")






db.close()


