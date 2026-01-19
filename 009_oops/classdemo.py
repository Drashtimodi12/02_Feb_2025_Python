
class Pen:

    __clg="drstc"
    # name="tops"

    def __init__(self,id,name):
       self.id = id
       self.name = name

    def display(self):
        print("dispay calling",self.id,self.name,self.__clg)
    
    def test(self):
        print("test calling")

    @classmethod
    def show(self):
        print("show calling",self.__clg)
    
    @staticmethod
    def run():
        print("run calling...")

Pen.__clg="abc"

p = Pen(10,"Akash")
p.display()

p1 = Pen(20,"Farukh")
p1.display()

p2 = Pen(30,"Rudra")
p2.display()

Pen.show()
Pen.run()



