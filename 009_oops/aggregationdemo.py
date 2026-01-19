
class Sample:

    def show(self):
        print("sample show calling")

class Demo:
    s = Sample()


d = Demo()
d.s.show()