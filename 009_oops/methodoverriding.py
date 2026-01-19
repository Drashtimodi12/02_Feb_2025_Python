
class A:

    def disp(self):
        print("class a displ calling")

class B(A):

    def disp(self):
        print("class b displ calling")

b  =B()
b.disp()