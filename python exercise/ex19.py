#create and print a list where the values are square of numbers between 1 and 30
def values():
    l=list()
    for i in range(1,30):
        l.append(i**2)
    print(l)
values()
