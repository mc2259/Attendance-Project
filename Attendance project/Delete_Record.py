import mysql.connector
db=mysql.connector.connect(user='root',password='',host='127.0.0.1',database='maitreyi')
cursor=db.cursor()
print('1.Delete from Course \n2. Delete Teacher \n3. Delete student  ')
choice=int(input('Enter choice:'))



if(choice==1):
    r=input('Enter CID of COURSE to be deleted: ')
    sql="DELETE FROM COURSE WHERE CID='%s'"%r
    
    try:
        cursor.execute(sql)
        db.commit()
        
        
    except:
        db.rollback()
        print('Record not deleted---')


    k=input('Delete corresponding student? ')
    if(k=='yes'):
        sql2="DELETE FROM STUDENT WHERE CID='%s'"%r
        try:
            cursor.execute(sql2)
            db.commit()
        except:
            db.rollback()
            print('Record not DELETED---')
    db.close()
if(choice==2):
    r=input('Enter SID of STUDENT to be deleted: ')
    sql="DELETE FROM STUDENT WHERE SID='%s'"%r
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
        print('Record not deleted---')
    
            
    
    db.close()
if(choice==3):
    r=input('Enter TID of TEACHER to be deleted: ')
    sql="DELETE FROM TEACHER WHERE TID='%s'"%r
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
        print('Record not DELETED---')
    db.close()

