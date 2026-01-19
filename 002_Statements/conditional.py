
# age = 17

# if age>=18 :
#     print("Elegeble for voting")
# else :
#     print("Not elegeble for voting")


a = 100
b = 100
c = 50

# if a>b:
#     if a>c:
#         print("A is greater")
#     else:
#         print("C is greater")
# else:
#     if b>c:
#         print("B is greater")
#     else:
#         print("C is greater")

# if a>b and a>c:
#     print("A is greater")
# elif b>a and b>c:
#     print("B is greater")
# elif c>a and c>b:
#     print("C is greater")
# else:
#     print("any two are same")


# marks = int(input("Enter marks : "))

# if marks>=90 and marks<=100:
#     print("Grade A")
# elif marks>=70 and marks<90:
#     print("Grade B")
# elif marks>=50 and marks<70:
#     print("Grade C")
# elif marks>=35 and marks<50:
#     print("Grade D")
# elif marks>=0 and marks<35:
#     print("Grade F")
# else:
#     print("Invalid input : enter marks between 0 to 100")

a = int(input("enter number a : "))
b = int(input("Enter number b : "))

c = int(input("""Enter choice : 
        1 : Add
        2 : sub
        3 : Mul
        4 : div
"""))

if c ==1:
    print("Addition is : ",(a+b))
elif c==2:
    print("substraction is : ",(a-b))
elif c==3:
    print("multiplication is : ",(a*b))
elif c==4:
    print("division is : ",(a/b))
else:
    print("Invalid choice")