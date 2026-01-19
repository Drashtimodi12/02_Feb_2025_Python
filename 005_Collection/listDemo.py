# list1 = ["Java","Python","Php","Android","Java"]
# list2 = ["Tops",123,145.56,True]
# list3 = list((10,20,30,40,50))

# print(list1[0])
# print(len(list1))
# print(type(list2))


#Access list
# fruits = ["Mango","Banana","Apple","Orange"]

# print(fruits[1])
# print(fruits[-2])
# print(fruits[1:3])
# print(fruits[2:])
# print(fruits[:3])
# print(fruits[-3:-1])
# print("Banana" in fruits)

#Change list items
# fruits = ["Mango","Banana","Apple","Orange"]
# # fruits[1] = "Kiwi"
# # fruits[1:3] = ["Kiwi","Grapes","sdsfd"]
# fruits.insert(1,"Kiwi")
# print(fruits)

#Add Items in list
# sports = ["Cricket","Football","Vollyball","Hockey","Tennis"]
# sports.insert(2,"Kabbaddi")
# sports.extend("abc")
# sports.extend(["chess","Carram","Ludo"])
# sports.extend(123) - Not possible

# print(sports)

#Remove list items
cars= ["Alto","Centro","Swift","jaz","innova","Fortuner"]

# cars.remove("Alto")
# cars.pop(3)
# cars.pop()
# del cars[1]
# del cars
# cars.clear()
# print(cars)

#Loop list

# for i in cars:
#     print(i)

# for i in range(len(cars)):
#     print(cars[i])


# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = []
# for i in fruits:
#     if "a" in i:
#         newlist.append(i)


# newlist = [i for i in fruits if "a" in i]
# newlist = [i.upper() for i in fruits if i != "apple"]
# newlist = ["abc" for i in fruits]

# newlist = [x if x != "banana" else "orange" for x in fruits]

# print(newlist)


fruits = ["apple", "banana", "kiwi", "mango","cherry"]

# fruits.sort(reverse=True)
# fruits.reverse()
# print(fruits)

# k = fruits.copy()
# k = list(fruits)
# print(k)


l1 = [1,2,3,4,5,2,2]
l2 = [10,20,30,40,50]

# l3 = l1+l2

# for a in l1:
#     l2.append(a)

# print(l2)

# print(l1.count(2))

# print(l1.index(5))

