print("program starting....")

try:

    #Zero division
    # a = 10
    # b = a/0
    # print(b)

    #Value Error
    # a = int(input("Enter a : "))
    # print(a)

    #IndexError
    # l = [10,20,30]
    # print(l[5])

    #KeyERr
    d = {"python":"1","Java":"2"}
    print(d["abc"])

except Exception as e:
    print(e)

# except ZeroDivisionError as a:
#     print(a)
# except ValueError as v:
#     print(v)
# else : 
#     print("else calling...")
# finally:
#     print("always executable....")

print("Program ended...")


