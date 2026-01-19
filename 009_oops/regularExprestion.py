import re

Nameage="""Rany is 2345 And Jeny is 65, Rany Tom is 85 and Roy is 42 """

# age = re.findall(r'\d{1,2}',Nameage)
# names=re.findall(r'[A-Z][a-z]*',Nameage)

# data = re.search("Rany",Nameage)
# data = re.match("Rany",Nameage)
# data = re.findall("Rany",Nameage)
# print(data)

# name="Python is world's best programming language "
# for i in re.finditer("world's",name):
#     print(i)
#   ans=i.span()
#   print(ans)


#tops@gmail.com
# p = "^[A-Za-z0-9]+@[a-z]+.[a-z]+$"

# r = re.match(p,"tops@gmail.com")
# if r is None:
#     print("Invalid email format")
# else:
#     print("Valid Format")


r  =re.match("^[0-9]{10}$","909999955")
if r is None:
    print("Invalid number")
else :
    print("valid number")