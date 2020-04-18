import importlib
flag=[0,0,0,0,0]
while True:               
    print("\n*** Main Menu ***")
    print("-----------------")
    print("1:DISPLAY RECORDS.")
    print("2:INSERT RECORD.")
    print("3:UPDATE RECORD.")
    print("4:DELETE RECORD.")
    print("5:SEARCH RECORD.")    
    print("6:EXIT.")
    choice=int(input("Enter your choice:"))
    if choice==1:        
        if flag[0]==0:
            import Display_Record      
            flag[0]=1
        else:
            importlib.reload(Display_Record)
    elif choice==2:
        if flag[1]==0:
            import Insert_Record       
            flag[1]=1
        else:
            importlib.reload(Insert_Record)            
    elif choice==3:
        if flag[2]==0:
            import Update_Record       
            flag[2]=1
        else:
            importlib.reload(Update_Record)
    elif choice==4:
        if flag[3]==0:
            import Delete_Record       
            flag[3]=1
        else:
            importlib.reload(Delete_Record)
    elif choice==5:
        if flag[4]==0:
            import Search_Record
            flag[4]=1
        else:
            importlib.reload(Search_Record)
    elif choice==6:                  
        print("Bye Bye...")        
        exit()
    else:
        print("Invalid choice. Press a no. between 1 to 6 only...")
