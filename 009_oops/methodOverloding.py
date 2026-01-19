from multipledispatch import dispatch

class Calc:

    # @dispatch(int , int)
    # def add(self,a,b):
    #     r = a+b
    #     print("m1 : ",r)
    
    # @dispatch(int, int, int)
    # def add(self,a,b,c):
    #     r = a+b+c
    #     print("m2 :",r)

    # @dispatch(int, float)
    # def add(self,a,b):
    #     r = a+b
    #     print("m3 :",r)

    def add(self,*a):
        sum = 0
        for i in a:
            sum+=i
        print(sum)

c = Calc()
c.add(10,20)
c.add(10,20,30)
c.add(30,45.00)