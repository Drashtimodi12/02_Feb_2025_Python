
a = 20  # blobal
def test():
    #global a
    a = 50
    a+=20
    print(a)


print("before : ",a)
test()
print("after : ",a)


