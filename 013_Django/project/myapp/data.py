import random
import string
from faker import Faker
fake = Faker()
from myapp.models import *

for i in range(10):
    username = fake.name()
    email= fake.email()
    phone =fake.phone_number()
    age = random.randint(21,30)
    
    Student.objects.create(
        username=username,
        email=email,
        phone=phone,
        age=age
    )