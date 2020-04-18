import mysql.connector
db=mysql.connector.connect(user='root',password='',host='127.0.0.1',database='maitreyi')
cursor=db.cursor()
choice=int(input('1. Update Course \n2. Update Student \n3. Update Teacher \n4.Enter Choice:  '))
if(choice==1):
    CID=input('Enter CID: ')
    
    CNAME=input('Enter CNAME:  ')
    DURATION=int(input('Enter duration: '))
    FEE=int(input('Enter fee: '))
    sql="UPDATE COURSE SET CNAME='%s' ,DURATION='%d', FEES='%d' WHERE CID='%s'"%(CNAME,DURATION,FEE,CID)
    try:
        cursor.execute(sql)
        db.commit()
        print('Record updated successfully')

    except:
        print('Record not updated ')
    db.close()


if(choice==2):
    SID=input('Enter SID: ')
    
    SNAME=input('Enter SNAME:  ')
    CID=input('Enter CID: ')
    MARKS=int(input('Enter MARKS: '))
    GRADE=input('Enter GRADE: ')
    sql="UPDATE STUDENT SET SNAME='%s' ,CID='%s', MARKS='%d', GRADE='%s' WHERE SID='%s'"%(SNAME,CID,MARKS,GRADE ,SID)
    try:
        cursor.execute(sql)
        db.commit()
        print('Record updated successfully')

    except:
        print('Record not updated ')
    db.close()

if(choice==3):
    CID=input('Enter CID: ')
    
    TNAME=input('Enter TNAME:  ')
    TID=input('Enter TID: ')
    
    sql="UPDATE `teacher` SET `TNAME`='%s',`CID`='%s' WHERE TID='%s'"%(TNAME,CID,TID)
    
    cursor.execute(sql)
    db.commit()
    print('Record updated successfully')

    
    db.close()
