

def call(a):
    print(a*a)
    a+=1
    if a<20:
        call(a)


call(10)