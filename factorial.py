n=int(input())
fact=1
if(n==0):
    print('factorial of o is 1')
elif(n<0):
    print('Invalid input')
else:
    while(n>0):
        fact=fact*n
        n=n-1
    print(fact)
