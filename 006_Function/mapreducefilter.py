
def square(a):
    b = int(a)
    return b*b

# l = [10,20,30,40,50,60]
# l1 = []
# for i in l:
#     k = square(i)
#     l1.append(k)
# print(l1)

# l1 = map(square,l)
# print(list(l1))

# l1 = list(map(square,(input("Enter number").split())))
# print(l1)


def add(x):
    return x+1

# def mul(x):
#     return x*2

# def apply(fun,x):
#     return fun(x)

# k = apply(add,10)
# l = apply(mul,20)
# print(k)
# print(l)


# l = [1,2,3,4,5]
# l1 = map(lambda x:x*x,l)
# print(list(l1))

a = [10,20,30,40,50,1,3,4,5]
b = [1,2,3,4,5]

# c  = map(lambda x,y:x+y,a,b)
# print(list(c))

from math import sqrt

# c = filter(lambda x:x%2!=0,a)
# print(list(c))

data = [1, 4, 6, 8, 9, 10, 12, 16, 81, 23, 36]  
# def isPreSquare(i):
#     return sqrt(i).is_integer()

# k = filter(isPreSquare,data)
# print(list(k))

from functools import reduce

# def add(x,y):
#     print(x,y)
#     return x*y

# c = reduce(add,data)
# c = reduce(lambda x,y:x+y,data)
# print(c)

def max(x,y):
    if x>y :
        return x
    else:
        return y

# k = reduce(max,data)
# k = reduce(lambda x,y: x if x<y  else y   ,data)
# print(k)

i = ["python","java","php","android"]

def isValid(x):
    if x.startswith('p'):
        return x
    

k = filter(isValid,i)
print(list(k))