#swapping two elements in a list
LIST=[44,56,78,32]
def swap(l,pos1,pos2):
    temp=l[pos1]
    l[pos1]=l[pos2]
    l[pos2]=temp
    return l
pos1,pos2=0,1
print(swap(LIST,pos1,pos2))
