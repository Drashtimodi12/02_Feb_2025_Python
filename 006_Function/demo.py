
def msg():
    print("Hello python")

def square(a):
    print(a*a)

def add(a,b):
    print(a+b)

def cube(a):
    return a*a*a

def stud(a=20,b="abc"):
    print(a,b)

def load(*a):
    sum = 0
    for i in a:
        sum+=i
    print(sum)

def show(**a):
    print(a)


# k = lambda a,b : a*b

# print(k(10,20))
# show(python="10",java="20",node=30)
# load(10,20,30,40,50,60)
# stud(10,"Drashti")
# stud(10,"ff")
# stud(b="xyz")
# msg()
# square(10)

# i = int(input("enter value of i: "))
# j = int(input("Enter value of j: "))
# add(i,j)
# k = cube(10)
# square(k)
