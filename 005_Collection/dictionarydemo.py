sub = {
    "java":"101",
    "python":"102",
    "Android":"102",
    "java":"ffdf"
}

# print(sub)

# print(sub['java'])

# print(len(sub))

# student = {
#     "name":"Rudra",
#     "email":"rudra@gmail.com",
#     "phone" : ["8574859685","74859968574"]
# }

# print(student['phone'][0])
# print(type(student))

# emp = dict(name="Akash",email="akash@gmail.com")
# print(emp)

# print(student.get("name"))

# x = student.keys()
# print(x)
# student['id'] = "10"
# print(x)

# x = student.values()
# print(x)
# student['name'] = "test"
# print(x)


# x = student.items()
# print(x)

# student.update({"address":"surat"})
# print(student)

# student['address']=["surat","Baroda"]
# print(student)

# student['address'].append("Amd")
# print(student)


# student.pop("name")
# student.popitem()
# print(student)

# for i in student:
#     print(i)

# for i in student:
#     print(student[i])

# for i in student.values():
#     print(i)

# for i in student.keys():
#     print(i)

# for x,y in student.items():
#     print(x,y)


student = {
    "name":"Rudra",
    "email":"rudra@gmail.com",
    "phone" : ["8574859685","74859968574"],
    "address" : {
        "city":"surat",
        "state":"gujarat",
        "country":"india"
    }
}

# print(student['address'].keys())

# for x,y in student.items():
#     print(x,y)

# for x,y in student['address'].items():
#     print(x,y)

x = student.setdefault("name1","abc")
print(x)
print(student)