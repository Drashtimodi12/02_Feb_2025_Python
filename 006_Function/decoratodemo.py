
# def before(func):
#     def wrap():
#         print(f"print before something....{func.__name__}")
#         func()
#         print("after somethnig...")
#     return wrap


# @before
# def test():
#     print("pring something...")


# @before
# def disp():
#     print("disp calling...")

# test()
# disp()


def add(func):
    def wrap(*a):
        sum =0
        for i in a:
            sum+=i
        print("Addition is : ", sum)
        func(*a)
    return wrap



@add
def result(a,b):
    print("Add calling....")


result(10,20)