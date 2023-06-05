#finding perfect number
def perfect_number(n):
    sum=0
    for i in range(1,n):
        if n%i==0:
            sum=sum+i

    if sum==n:
        print(n)
print(perfect_number(7))
        
