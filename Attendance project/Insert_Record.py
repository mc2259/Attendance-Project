import importlib
import mysql.connector
db=mysql.connector.connect(user='root',password='',host='127.0.0.1',database='maitreyi')
choice=int(input('1.Insert into Course \n2. Insert into Student \n3. Insert into attendance \n4.Insert into Teacher \n5. Enter Choice: '))

cursor=db.cursor()
if(choice==1):
    CID=input("Enter CID:  ")
    CNAME=input('Enter CNAME: ')
    DURATION=int(input('Enter DURATION '))
    FEES=int(input('Enter FEES '))
    sql=" INSERT INTO COURSE VALUES('%s','%s','%d','%d')"%(CID,CNAME,DURATION,FEES)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
        print(" Record not saved---")
    import Display_Record
    db.close()        
        

elif(choice==2):
    SID=input("Enter SID:  ")
    SNAME=input('Enter SNAME: ')
    CID=input('Enter CID: ')
    MARKS=int(input('Enter MARKS: '))
    GRADE=input('Enter GRADE:  ')
    sql=" INSERT INTO STUDENT VALUES('%s','%s','%s','%d','%s')"%(SID,SNAME,CID,MARKS,GRADE)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
        print(" Record not saved---")
    import Display_Record
    db.close()        
elif(choice==3):
    SL_NO=int(input("Enter SL_NO:  "))
    SID=input('Enter SID: ')
    DATE=input('Enter DATE: ')
    STATUS=input('Enter STATUS: ')
    START_TIME=input('Enter START_TIME:  ')
    END_TIME=input('Enter END_TIME:  ')
    sql=" INSERT INTO ATTENDANCE VALUES('%d','%s','%s','%s','%s','%s')"%(SL_NO,SID,DATE,STATUS,START_TIME,END_TIME)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
        print(" Record not saved---")
    import Display_Record
    db.close()

elif(choice==4):
    TID=input("Enter TID:  ")
    TNAME=input('Enter TNAME: ')
    CID=input('Enter CID: ')
    
    
    sql=" INSERT INTO TEACHER VALUES('%s','%s','%s)"%(TID,TNAME,CID)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
        print(" Record not saved---")
    import Display_Record
    db.close()                

