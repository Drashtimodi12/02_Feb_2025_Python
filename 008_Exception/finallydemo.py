
def test():
    try:
        a = int(input("enter number : "))
        return 1
    except Exception as e:
        return 0
    finally:
        print("Pring in th function...")



k = test()
print(k)