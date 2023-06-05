class student:
    pass
class marks:
    pass
s=student()
m=marks()
print(isinstance(s,student))
print(isinstance(m,student))
print(isinstance(s,marks))
print(isinstance(m,marks))
print(issubclass(student,object))
print(issubclass(marks,object))
