import customer as c 
import banker as b

choice=0
while choice!=3:
    print("""
            WELCOME TO PYTHON BANK MANAGEMENT SYSTERM
            Select your role : 
            1 : Banker
            2 : Customer
            3 : Exit
    """)
    choice = int(input("Chose your role : "))
    if choice==1:
        b.bankerOperations()
    elif choice==2:
        c.customerOperations()
    elif choice==3:
        print("You are Exit !!!")
    else :
        print("Invalid choice")