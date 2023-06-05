def palindrome(num):
   
    original_number = num
    reverse_number = original_number
    if original_number==reverse_number:
        
        return True
    else:
        return False

num=int(input("enter your number"))
   
if palindrome(num):
    print(num,"palindrome")
else:
    print(num,"not palindrome")

    
