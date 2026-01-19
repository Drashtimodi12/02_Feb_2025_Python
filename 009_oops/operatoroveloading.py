

class Demo:

    def __init__(self,a,b):
        self.a = a
        self.b = b
    
    def __add__(self,obj):
        return self.a+obj.a,self.b+obj.b

    
    def __mul__(self,obj):
        return self.a*obj.a,self.b*obj.b


d1 = Demo(10,20)
d2 = Demo(20,40)

c = d1*d2
print(c)