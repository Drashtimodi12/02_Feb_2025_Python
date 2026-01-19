
def bankerOperations():
    customers = {}
    choice='Y'
    while choice !='N':
        print(""" 
        Welcome to banker's App 
            Operations menu :
            1 : Add Customer
            2 : View Customer
            3 : Search customer
            4 : Total amount in Bank
        """)
        op = int(input("Enter operation which you want to do : "))
       
        if op==1:
            ano = input("enter acount number : ")
            name = input("enter customer name : ")
            balance = input("enter opening balance")
            customers.update({ano:{"name":name,"balance":balance}})
            print(customers)
        elif op==2:
            print(customers)

        choice = input("do you want to performe more operations ? Y or N :")