from faker import Faker
fake = Faker()
import random
from app.models import *
def generate(n=50):
    for i in range(n):
        alldepts = Department.objects.all()
        dept = alldepts[random.randint(0,len(alldepts)-1)]
        name = fake.name()
        email = fake.email()
        age = random.randint(21,30)
        stid = f"STD_{random.randint(100,999)}"
        studentid =  StudentId.objects.create(stid=stid)
        Student.objects.create(dept=dept,stid=studentid,name=name,email=email,age=age)
       
def setMarks():
    allstudents = Student.objects.all()
    for student in allstudents:
        allsubjects = Subject.objects.all()
        for subject in allsubjects:
            Marks.objects.create(student=student,subject=subject,marks=random.randint(1,100))
