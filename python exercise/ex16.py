#function that takes two lists and return true if they have at least one common member
def two_list(l1,l2):
    for x in l1:
        #print("commom element")
        for y in l2:
            #print("no common element")
            if x == y:
                result = True
                return result
print(two_list([8,9,10,57,58],[10,58,59,68,78]))
print(two_list([88,99,106,57,98],[10,58,59,68,78]))
      
