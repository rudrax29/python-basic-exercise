#DETERMINE WHETHER ALL THE NUMBERS ARE DIFFERENT FROM EACH OTHER
def numbers(NUMBERS):

        if len(NUMBERS)==len(set(NUMBERS)):
            return True
        else:
            return False
    

print(numbers([4,5,7,8,8,9]))
print(numbers([89,90,98,97,95,78]))
